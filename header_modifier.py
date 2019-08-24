# -*- coding: utf-8 -*-
"""
Created on Jul 11, 2016
Modifies passed text for file name
@author: Levan Tsinadze
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys

SEPARATOR = '_'

SPCS = ['-', '.', ',', ':', ';', '!', '?', '"', '\\', '/', '(', ')', '{', '}', '[', ']']
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

        for ch in tx:
            if ch in SPCS:
                itm += SEPARATOR
            elif ch not in DLTS:
                itm += ch

        return itm

    def generate_name(self, raw_text):
        """
        Generates appropriated file name from raw text
        Args:
            raw_text: text for file name generator

        Returns:
            fl_name: generated file name
        """
        fl_name = ''

        length = len(raw_text) - 1
        for idx, tx in enumerate(raw_text):
            if idx > 0:
                fl_name += self.generate_item(tx.lower())
                if idx < length and not fl_name.endswith(SEPARATOR):
                    fl_name += SEPARATOR

        return fl_name


class PDFNameGenerator(FileNameGenerator):
    """Generates PDF file name from article"""

    def __init__(self, *args, **kwargs):
        super(PDFNameGenerator, self).__init__(*args, **kwargs)

    def generate_pdf_name(self, raw_text):
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


if __name__ == '__main__':
    """Modify text for file name"""
    gen = FileNameGenerator()
    file_name = gen.generate_name(sys.argv)
    print(file_name)
    if len(sys.argv) > 2:
        gen = PDFNameGenerator()
        file_name = gen.generate_pdf_name(sys.argv)
        print(file_name)
