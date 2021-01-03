#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""PySimpleFrame
   Name: TOFILL
   Author: Miguel Silva
   Description: TOFILL
   License: CC BY-SA 4.0 - Check LICENSE file
"""

## System imports ##
import sys

## Library imports ##


## Application imports ##
from interface.input.Input import Input


class KeyPreset:
	def __init__(self, keys):
		self.keys = keys
		
		self.index = -1
	
	def __del__(self):
		del self.keys
		del self.index
	
	def Index(self):
		return self.index
	
	def Input(self):
		input = Input.GetInput()
		index = Input.GetKeyIndex(input)
		key = Input.InputIdxToKeyCode(index)
		
		try:
			self.index = self.keys.index(key)
		except:
			self.index = -1
		
		return self.index
		
		