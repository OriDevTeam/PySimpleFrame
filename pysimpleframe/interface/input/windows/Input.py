#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""PySimpleFrame
   Name: TOFILL
   Author: Miguel Silva
   Description: TOFILL
   License: Check LICENSE file
"""

## System imports ##
import msvcrt

## Library imports ##

## Application imports ##



class Input:
	def GetCharacter():
		return msvcrt.getch()
	
	@classmethod
	def GetInputBytes(cls):
		## Convert key code input into commands
		k = bytearray()
		
		## Get characters while keyboard is hit
		while(True):
			## Get inputed character to bytes
			l = bytes(cls.GetCharacter())
			
			## Add inputed bytes to byte array
			k += l
			
			## Break if there is no more keyboard input
			if not msvcrt.kbhit(): break
		
		## Return character bytes array into bytes
		return bytes(k)
	
	@classmethod
	def GetInput(cls):
		## Get input bytes, parse to string and return
		return repr(bytes(cls.GetInputBytes()))[2:-1]
	
		