#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""PySimpleFrame
   Name: TOFILL
   Author: Miguel Silva
   Description: TOFILL
   License: Check LICENSE file
"""

## System imports ##
import os
import sys

## Library imports ##
from colorama import Fore, Back, Style

## Application imports ##

class CLI:
	def GetBounds():
		## Get the bounds of the terminal window
		rows, columns = os.popen('stty size', 'r').read().split()
		
		## Return the bounds
		return rows, columns
	
	def SetBounds(rows, cols):
		## Set the bounds of the terminal window
		sys.stdout.write(f"\x1b[8;{rows};{cols}t")

class CLIWindows:
	def SetBounds(rows, cols):
		## Set the bounds of the terminal window in Windows
		os.system(f'mode con: cols={cols} lines={rows}')
