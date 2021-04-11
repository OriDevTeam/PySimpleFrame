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
import Input
from KeyCodes import KeyCodes


## Print state
print("Listening input (press CTRL+C twice to stop)")


## Capture key inputs continuously
lastInput = None
while True:
	## Wait for input and set
	input = Input.GetInput()
	
	## Print input
	print(f"Inputed: {input}")
	
	## Break if CTRL + C was pressed now and before
	if lastInput == KeyCodes.COPYCANCEL.keycode() and input == KeyCodes.COPYCANCEL.keycode():
		print("Input listening canceled")
		break
	
	## Set last input as current input
	lastInput = input
	
	