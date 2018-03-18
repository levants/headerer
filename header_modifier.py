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
DLTS = ['\'']


class file_name_generator(object):
  """File name generator"""
  
  def generate_item(self, tx):
    """Generates item from string
      Args:
        tx - input string
      Returns:
        itm - item from string
    """
    itm = ''
    
    for ch in tx:
      if ch in SPCS:
        itm += SEPARATOR
      elif ch not in DLTS:
        itm += ch
     
    return itm
  
  def generate_name(self, raw_text):
    """Generates appropriated file name from raw text
      Args:
        raw_text - text for file name generator
      Returns:
        file_name - generated file name
    """
    
    file_name = ''
    
    i = 0
    length = len(raw_text) - 1
    for tx in raw_text:
      if i > 0:
        file_name += self.generate_item(tx.lower())
        if i < length and not file_name.endswith(SEPARATOR):
          file_name += SEPARATOR
      i += 1
    
    return file_name

  
class pdf_name_generator(file_name_generator):
  """Generates PDF file name from article"""
  
  def __init__(self, *args, **kwargs):
    file_name_generator.__init__(self, *args, **kwargs)
  
  def generate_pdf_name(self, raw_text):
    
    file_name = file_name_generator.generate_name(self, raw_text)
    pdf_name = file_name + ".pdf"
    
    return pdf_name

  
if __name__ == '__main__':
  
  gen = file_name_generator()
  file_name = gen.generate_name(sys.argv)
  print(file_name)
  if len(sys.argv) > 2:
    gen = pdf_name_generator()
    file_name = gen.generate_pdf_name(sys.argv)
    print(file_name)
    
