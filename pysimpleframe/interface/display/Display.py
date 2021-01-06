#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Name: Display CLI Module\n
   Description: Handles the control of display of text in CLI
"""

"""PySimpleFrame
   Author: Miguel Silva
   License: Check LICENSE file
"""

## System imports ##
import sys

## Library imports ##
from colorama import init, Fore, Back, Style

## Application imports ##
from .Bounds import CLI


def Initialize():
	"""Initializes the CLI interface display (run once per application instance)"""
	
	## Initialize colorama
	init(autoreset=True)
	
	## Create global clear count variable for display lines count to clear
	global CLEAR_COUNT
	CLEAR_COUNT = 0
	
	## Set terminal size
	CLI.SetBounds(25, 110)

def Change(amount):
	"""Changes the count of printed lines by summing up
	
	:param amount: Amount to sum up to the current count
	:type amount: int
	"""
	
	## Reference the counting variable
	global CLEAR_COUNT
	
	CLEAR_COUNT += amount

def PrintCount():
	"""Prints the count of printed count"""
	
	## Reference the counting variable
	global CLEAR_COUNT
	
	## Print the current clear count
	Print(str(CLEAR_COUNT + 1))

def Print(message, e='\n'):
	"""
	Prints a line and tracks the amount
	
	:param message: Message to print to STDOUT
	:type message: str
	:param e: Ending string for the message
	:type e: str
	"""
	
	## Cast the message into string to be sure
	message = str(message)
	
	## Reference the counting variable
	global CLEAR_COUNT
	
	## Add the clear count of newlines in the message
	CLEAR_COUNT += message.count('\n')
	
	## Add the clear count of newlines in the message ending
	CLEAR_COUNT += e.count('\n')
	
	## Print the message
	print(message, end=e)
	
def ClearDisplay():
	"""Clears the amount of tracked lines printed from STDOUT"""
	
	## Reference the counting variable
	global CLEAR_COUNT
	
	## Clear the specified amount of lines
	for x in range(0, CLEAR_COUNT): ClearPreviousLine()
	
	#Print("Cleared %i lines" % CLEAR_COUNT)
	
	## Reset the counting lines
	CLEAR_COUNT = 0

def ClearPreviousLine():
	"""Deletes the last line from STDOUT"""
	
	## Put the Cursor up one line
	sys.stdout.write('\x1b[1A')

	## Delete last line
	sys.stdout.write('\x1b[2K')

