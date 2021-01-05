#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""PySimpleFrame
   Name: TOFILL
   Author: Miguel Silva
   Description: TOFILL
   License: Check LICENSE file
"""

## System imports ##
from enum import Enum, IntEnum, unique

## Library imports ##

## Application imports ##


@unique
class KeyCodes(Enum):
	NONE 		= (0, 'NONE', 		 '')
	
	## Directions (100 - 200
	LEFT 		= (100, 'LEFT',  	 '\\xe0M')
	RIGHT 		= (101, 'RIGHT', 	 '\\xe0K')
	UP 			= (102, 'UP', 	 	 '\\xe0H')
	DOWN 		= (103, 'DOWN',  	 '\\xe0P')
	
	## Actions (200 - 300)
	ENTER 		= (200, 'ENTER', 	 '\\r')
	BACKSPACE 	= (201, 'BACKSPACE', '\\x08')
	ESCAPE 		= (202, 'ESCAPE', 	 '\\x1b')
	SPACE 		= (203, 'SPACE', 	 ' ')
	TAB			= (204, 'TAB', 		 '\\t')
	
	## Control combinations (300 - 400)
	SELECTALL	= (300, 'SELECTALL', '\\x01')
	SWITCH		= (301, 'SWITCH', 	 '\\x02')
	COPYCANCEL 	= (302, 'COPYCANCEL','\\x03')
	UNK1		= (303, 'UNK1', 	 '\\x04')
	UNK2		= (304, 'UNK2', 	 '\\x05')
	SAVE		= (305, 'SAVE', 	 '\\x13')
	UNDO		= (306, 'UNDO', 	 '\\x1a')
	REDO		= (307, 'REDO', 	 '\\x19')
	PASTE 		= (308, 'PASTE', 	 '\\x16')
	
	## Alphabet - Lower case (400 - 500)
	a 			= (400, 'a', 		 'a')
	b 			= (401, 'b', 		 'b')
	c			= (401, 'c', 		 'c')
	
	## Alphabet - Upper case (400 - 500)
	A 			= (500, 'A', 		 'A')
	B 			= (501, 'A', 		 'B')
	C			= (502, 'C', 		 'C')
	
	def keyindex(self):
		return self.value[0]
	
	def keyname(self):
		return self.value[1]
	
	def keycode(self):
		return self.value[2]
	
	@staticmethod
	def list():
		return list(KeyCodes)
	
	@staticmethod
	def vlist():
		return list(map(lambda k: k.value, KeyCodes))
	
	def __index__(self):
		return self.value - 1

	def __int__(self):
		return self.value - 1

## Replace the locals with the keys codes
#locals = KeyCodes.list()

