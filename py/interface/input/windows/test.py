#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""PySimpleFrame
   Name: TOFILL
   Author: Miguel Silva
   Description: TOFILL
   License: CC BY-SA 4.0 - Check LICENSE file
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
	
	