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
from enum import Enum, IntEnum, unique

## Library imports ##

## Application imports ##


@unique
class KeyCodes(Enum):
	NONE 		= (0, 'NONE', 		 '')
	
	## Directions (100 - 200
	LEFT 		= (100, 'LEFT',  	 '\x1b[D')
	RIGHT 		= (101, 'RIGHT', 	 '\x1b[C')
	UP 			= (102, 'UP', 	 	 '\x1b[A')
	DOWN 		= (103, 'DOWN',  	 '\x1b[B')
	
	## Actions (200 - 300)
	ENTER 		= (200, 'ENTER', 	 '\n')
	BACKSPACE 	= (201, 'BACKSPACE', '\x7f')
	ESCAPE 		= (202, 'ESCAPE', 	 '\x1b')
	SPACE 		= (203, 'SPACE', 	 ' ')
	TAB			= (204, 'TAB', 		 '\t')
	
	## Clipboard (300 - 400)
	PASTE 		= (300, 'PASTE', 	 '\x16')
	
	## Alphabet (400 - 500)
	A 			= (400, 'A', 		 'a')
	Q			= (401, 'Q', 		 'q')
	
	def keyname(self):
		return self.value[1]
	
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

