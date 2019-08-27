# -*- coding: utf-8 -*-
"""
Created on Jul 11, 2016
Modifies passed text for file name
@author: Levan Tsinadze
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os

SEPARATOR = '_'

SPCS = [' ', '-', '.', ',', ':', ';', '!', '?', '"', '\\', '/', '(', ')', '{', '}', '[', ']']
DLTS = ['\'', '-', u'–', '+']


class FileNameGenerator(object):
    """File name generator"""

    def __init__(self, *args, **kwargs):
        super(FileNameGenerator, self).__init__(*args, **kwargs)

    @staticmethod
    def generate_item(tx):
        """
        Generates item from string
        Args:
            tx: input text to modify

        Returns:
            itm: next item from existing text
        """
        itm = ''

        for idx, ch in enumerate(tx):
            if ch in SPCS:
                itm += SEPARATOR if idx < len(tx) - 1 else ''
            elif ch not in DLTS:
                itm += ch

        return itm

    def generate_name(self, raw_texts: list) -> str:
        """
        Generates appropriated file name from raw text
        Args:
            raw_texts: texts for file name generator

        Returns:
           generated file name
        """
        return '_'.join(
            self.generate_item(raw_text.lower()) if raw_text and raw_text.strip() else '' for raw_text in raw_texts)


class PDFNameGenerator(FileNameGenerator):
    """Generates PDF file name from article"""

    def __init__(self, *args, **kwargs):
        super(PDFNameGenerator, self).__init__(*args, **kwargs)

    def generate_pdf_name(self, raw_text: str) -> str:
        """
        Generates file name for PDF file type
        Args:
            raw_text: input text

        Returns:
            pdf_name: generated PDF file name
        """
        fl_name = FileNameGenerator.generate_name(self, raw_text)
        pdf_name = fl_name + '.pdf'

        return pdf_name


def config():
    """
    Configure for input text
    Returns:
        conf: command line configuration parameters
    """
    parser = argparse.ArgumentParser('File name generator from header')
    parser.add_argument('--header',
                        nargs='+',
                        type=str,
                        required=True,
                        help='Text to generate file name')
    parser.add_argument('--pdf',
                        dest='pdf',
                        action='store_true',
                        help='Flag to generate file name with PDF extension')
    conf = parser.parse_args()

    return conf


if __name__ == '__main__':
    """Modify text for file name"""
    cf = config()
    gen = FileNameGenerator()
    file_name = gen.generate_name(cf.header)
    os.system(f'echo {file_name}| pbcopy')
    print(file_name)
    if cf.pdf:
        pdf_name = file_name + '.pdf'
        print(pdf_name)
