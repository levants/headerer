# -*- coding: utf-8 -*-
"""
Created on Jul 11, 2016
Modifies passed text for file name
@author: Levan Tsinadze
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import unittest

from header_modifier import FileNameGenerator, DLTS, ACCP


class TestHeaderModifier(unittest.TestCase):
    """Test cases for header generator"""

    def setUp(self) -> None:
        self.hederer = FileNameGenerator()
        self.raw_txt = """Not Using the Car to See the Sidewalk — Quantifying 
                             and Controlling the Effects of Context in Classification and Segmentation"""

    def test_generator(self):
        """Test header generator"""
        print(sorted(ACCP))
        header_txt = self.hederer(self.raw_txt)
        assert not set(header_txt).intersection(DLTS)
        print(f'header_txt = {header_txt}')
