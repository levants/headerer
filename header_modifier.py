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

# Static parameters
SEPARATOR = '_'

SPCS = {' ', '-', '–', '+', '.', ',', ':', ';', '!', '?', '"', '\'', '\\', '/', '(', ')', '{', '}', '[', ']', '\\n',
        '\\t'}
DLTS = {'\'', '-', '–', '+'}
ACCP = {f(chr(x)) for x in range(ord('a'), ord('z') + 1) for f in [lambda x: x, lambda x: x.upper()]}.union(
    {str(x) for x in range(0, 10)})


class FileNameGenerator(object):
    """File name generator"""

    def __init__(self, *args, **kwargs):
        super(FileNameGenerator, self).__init__(*args, **kwargs)

    @staticmethod
    def _iterate_text(tx: str) -> str:
        sep_ch = False
        for idx, ch in enumerate(tx):
            if ch in ACCP:
                next_ch = ch.lower()
                sep_ch = True
            elif idx < len(tx) - 1 and sep_ch:
                next_ch = SEPARATOR
                sep_ch = False
            else:
                next_ch = ''
                sep_ch = False

            yield next_ch

    @staticmethod
    def generate_item(tx: str) -> str:
        """
        Generates item from string
        Args:
            tx: input text to modify

        Returns:
            itm: next item from existing text
        """
        return ''.join(ch for ch in FileNameGenerator._iterate_text(tx))

    def generate_name(self, *raw_texts: str) -> str:
        """
        Generates appropriated file name from raw text
        Args:
            raw_texts: texts for file name generator

        Returns:
           generated file name
        """
        return ''.join(self.generate_item(' '.join(raw_texts)))

    def __call__(self, *args, **kwargs):
        return self.generate_name(*args, **kwargs)


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
    parser = argparse.ArgumentParser('File name generator from header', formatter_class=argparse.RawTextHelpFormatter)
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
    file_name = gen(*cf.header)
    os.system(f'echo {file_name}| pbcopy')
    print(file_name)
    if cf.pdf:
        pdf_name = file_name + '.pdf'
        print(pdf_name)
