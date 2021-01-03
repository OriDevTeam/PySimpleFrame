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
from colorama import Fore, Back, Style

## Application imports ##
from interface.display import Display
from interface.input.KeyCodes import KeyCodes
from interface.input import KeyPreset


class Menu:
	"""Interactive select menu.

	Attributes:
		opts (list of str): Options for the user to choose from.
	"""
	opts = []

	def __init__(self, options, message):
		"""Interactive select menu.

		Args:
			options (list of str): Options for the user to choose from.
			message (str, optional): Message to be displayed before showing options
		"""
		
		self.opts = options
		
		if message:
			print(message)
			
	
	def _DisplayHints(self):
		## Show action hints if enabled
		#hint = Fore.YELLOW + "Use arrow keys" + Fore.GREEN + " <- -> " + Fore.YELLOW + "to change, press" + Fore.GREEN + " ENTER " + Fore.YELLOW + "to select "
		#hint += Fore.YELLOW + "or press " + Fore.RED + "CTRL + C" + Fore.YELLOW + " to Quit"
		
		hint = Fore.YELLOW + "Use arrow keys" + Fore.GREEN + " ▲ ▼ " + Fore.YELLOW + "to change, "
		hint +=	"press" + Fore.GREEN + " ENTER " + Fore.YELLOW + "to select, "
		hint +=	"press" + Fore.GREEN + " BKSPC " + Fore.YELLOW + "to end selection "
		hint += Fore.YELLOW + "or press " + Fore.RED + "CTRL + C" + Fore.YELLOW + " to Quit"
		
		#hint = Fore.YELLOW + "Use arrow keys" + Fore.GREEN + " <- -> Change |"
		#hint += Fore.YELLOW + "" + Fore.GREEN + " ENTER " + Fore.YELLOW + " Select |"
		#hint += Fore.YELLOW + "" + Fore.GREEN + " ESC " + Fore.YELLOW + " Go back |"
		#hint += Fore.YELLOW + "" + Fore.RED + " CTRL + C " + Fore.YELLOW + "Quit"
		
		print(hint)
	
	def _ClearHints(self):
		## Clear previous hints
		Display.ClearPrevLine()

class VerticalMenu(Menu):
	def __init__(self, options, message=None):
		Menu.__init__(self, options, message)
		
		## Make an instance of a Key Preset with the chosen Key Codes
		self.keyPreset = KeyPreset.KeyPreset([KeyCodes.UP, KeyCodes.DOWN, KeyCodes.BACKSPACE, KeyCodes.ENTER, KeyCodes.NONE])
		
	def __call__(self, numbered, hints):
		"""Creates an interactive select menu for the user. The user's choice is selected with up/down/left/right arrow keys and confirmed with the enter/return key.

		Returns:
			Option (from list) selected by user.
		"""
		
		return self.__DisplayMenu(numbered, hints)
	
	def __DisplayMenu(self, numbered, hints):
		## Declare the selected option index
		selected = 0
		
		## Declare the selected options indexes
		selectedIndexes = []
		
		## Declare the state of the options picking
		done = False
		
		## Infinite loop broken by return
		while True:
			for ind, opt in enumerate(self.opts):
				## If option is a list get the description
				if isinstance(opt, list):
					value = opt[0]
					description = opt[1]
				else:
					value = opt
				
				## Add the option index number if enabled
				if numbered:
					op 
					op = "%i - %s" % (ind + 1, value)
				else:
					op = value
				
				## Create the item text
				option = ""
				
				## Append color if its selected
				if ind == selected: option += Fore.GREEN
				
				## Append the selected/unselected tag
				if ind in selectedIndexes:
					option += "[X] "
				else:
					option += "[ ] "
				
				## Append the option
				option += op.ljust(self.__MaxPropertyLength(), " ")
				
				## Append the description
				option += "  %s" % description
				
				## Display the option
				print(option)
				
			
			# Forcing options to show (would be delayed until after keypress in Python 3)
			sys.stdout.flush()
			
			print("")
			
			## Display Hints
			if hints: self._DisplayHints()
			
			## Catch pressed key and option
			opt = None
			key_pressed = None
			while key_pressed == None:
				## Get key preset input index from user
				key_pressed = self.keyPreset.Input()
				
				if key_pressed == 1 and selected < len(self.opts) - 1:
					selected += 1
				elif key_pressed == 0 and selected > 0:
					selected -= 1
				elif key_pressed == 2:
					done = True
				elif key_pressed == 3:
					if not selected in selectedIndexes:
						selectedIndexes.append(selected)
					else:
						selectedIndexes.remove(selected)
				elif key_pressed == 4:
					done = True
			
			## Clear the text
			self.Clear(hints)
			
			## Return if its done selecting
			if done:
				#Display.ClearPrevLine()
				return selectedIndexes
				
	
	def Clear(self, hints):
		## Clear hints
		if hints: self._ClearHints()
		
		## Clear the previously displayed options
		Display.ClearPrevLine()
		
		for i in range(0, len(self.opts)):
			Display.ClearPrevLine()
	
	def __MaxPropertyLength(self):
		length = 0
		
		for option in self.opts:
			opt = option[0]
			if len(opt) > length:
				length = len(opt)
		
		return length
	
		