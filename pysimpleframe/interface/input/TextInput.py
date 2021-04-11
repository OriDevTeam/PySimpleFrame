#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Name: TOFILL\n
   Description: TOFILL
"""

"""PySimpleFrame
   Author: Miguel Silva
   License: Check LICENSE file
"""

## System imports ##
import sys

## Library imports ##


## Application imports ##
from pysimpleframe.interface.input import Input


class TextInput:
	def __init__(self, keys):
		## Reference the keys
		self.Keys = keys
		
		## Reference the current index
		self.Index = -1
		
		## Reference the inputed character
		self.InputChr = ""
	
	def __del__(self):
		del self.Keys
		del self.Index
		del self.InputChr
	
	def Input(self):
		## Get the input
		input = Input.GetInput()
		
		## Get the index from input
		index = Input.GetKeyIndex(input)
		
		## Get the key from input index
		key = Input.InputIdxToKeyCode(index)
		
		## Set the current preset index from key
		try:
			self.Index = self.Keys.index(key)
		except:
			self.Index = -1
		
		## Set the current input
		self.InputChr = input
		
		## Return the index
		return self.Index
		
		