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
import os

## Library imports ##

## Application imports ##
from compatibility.Compatibility import OperativeSystem

## Import input according to detected OS
if OperativeSystem.IsWindows():
	from interface.input.windows.KeyCodes import KeyCodes
	from interface.input.windows.Input import Input as BInput
else:
	from interface.input.linux.KeyCodes import KeyCodes
	from interface.input.linux.Input import Input as BInput


class Input(BInput):
	def GetKeyIndex(key):
		## Reference the index
		idx = 0
		
		## Iterate trough key codes list and return index if found
		for keycode in KeyCodes.vlist():
			if keycode[2] == key:
				return idx
			
			idx += 1
		
		## If not found return 0(none)
		return 0
	
	def GetIndexOfKey(keyIndex):
		## Register the index
		idx = 0
		
		## Iterate trough key codes list and return index if found
		for keycode in KeyCodes.vlist():
			if keycode[0] == keyIndex:
				return idx
			
			idx += 1
		
		## If not found return 0(none)
		return 0
	
	def InputIdxToKeyCode(index):
		return KeyCodes.list()[index]
	
	def GetInputKey():
		return InputIdxToKeyCode(GetKeyIndex(GetInput()))

	def GetKeyCodeFromInput(chr):
		return InputIdxToKeyCode(GetKeyIndex(chr))
	