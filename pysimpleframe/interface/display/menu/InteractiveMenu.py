#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""PySimpleFrame
   Name: TOFILL
   Author: Miguel Silva
   Description: TOFILL
   License: Check LICENSE file
"""

## System imports ##
import sys
import time

## Library imports ##
from colorama import init, Fore, Back, Style

## Application imports ##
from pysimpleframe.display import Display
from pysimpleframe.input.KeyCodes import KeyCodes
from pysimpleframe.input.TextInput import TextInput
from pysimpleframe.input import Input as KeyInput


class Menu:
	"""Interactive select menu.

	Attributes:
		opts (list of str): Options for the user to choose from.
	"""
	opts = []

	def __init__(self, itemList, message):
		"""Interactive select menu.

		Args:
			options (list of str): Options for the user to choose from.
			message (str, optional): Message to be displayed before showing options
		"""
		
		self.itemList = itemList
		
		if message:
			print(message)
			
	
	def _DisplayHints(self):
		## Show action hints if enabled
		#hint = Fore.YELLOW + "Use arrow keys" + Fore.GREEN + " <- -> " + Fore.YELLOW + "to change, press" + Fore.GREEN + " ENTER " + Fore.YELLOW + "to select "
		#hint += Fore.YELLOW + "or press " + Fore.RED + "CTRL + C" + Fore.YELLOW + " to Quit"
		
		hint = Fore.YELLOW + "Use arrow keys" + Fore.GREEN + " <- -> " + Fore.YELLOW + "to change, "
		hint +=	"press" + Fore.GREEN + " ENTER " + Fore.YELLOW + "to select, "
		hint +=	"press" + Fore.GREEN + " BKSPC " + Fore.YELLOW + "to go back "
		hint += Fore.YELLOW + "or press " + Fore.RED + "CTRL + C" + Fore.YELLOW + " to Quit"
		
		#hint = Fore.YELLOW + "Use arrow keys" + Fore.GREEN + " <- -> Change |"
		#hint += Fore.YELLOW + "" + Fore.GREEN + " ENTER " + Fore.YELLOW + " Select |"
		#hint += Fore.YELLOW + "" + Fore.GREEN + " ESC " + Fore.YELLOW + " Go back |"
		#hint += Fore.YELLOW + "" + Fore.RED + " CTRL + C " + Fore.YELLOW + "Quit"
		
		print(hint)
	
	def _ClearHints(self):
		## Clear previous hints
		Display.ClearPreviousLine()
	
class Input:
	def __init__(self, property, default="", description=""):
		## Reference the property
		self.Property = property
		
		## Reference the value and set the default
		self.Value = default
		
		## Reference the description
		self.Description = description
		
		## Reference the max property length
		self.MaxPropertyLength = 20 + 1 ## Extra colon characters
		
		## Reference the max value length
		self.MaxValueLength = 12
	
	def __del__(self):
		pass
	
	def Change(self, chr):
		if KeyInput.GetKeyCodeFromInput(chr) == KeyCodes.BACKSPACE:
			if len(self.Value) > 0:
				self.Value = self.Value[:-1]
		else:
			if len(self.Value) < self.MaxValueLength:
				self.Value += chr
	
	def FieldText(self, selected):
		text = self.Property + ":"
		text = text.ljust(self.MaxPropertyLength)

		## If selected add a check mark
		if selected:
			value = self.Value + "✓"
		else:
			value = self.Value
		
		text += value
		
		return text
	
	def AllText(self, selected):
		text = self.FieldText(selected)
		
		desc = " " + self.Description
		
		text += desc.rjust(len(desc) + self.MaxLength() - len(text))
		
		return text
	
	def MaxLength(self):
		return self.MaxPropertyLength + self.MaxValueLength + 1 ## Extra check mark character

class CheckBox:
	def __init__(self, property, default=False, description=""):
		## Reference the property
		self.Property = property
		
		## Reference the check and set the default
		self.Checked = default
		
		## Reference the description
		self.Description = description
		
		## Reference the max property length
		self.MaxPropertyLength = 20 + 1 ## Extra colon characters
		
		## Reference the max value length
		self.MaxValueLength = 12
		
	def __del__(self):
		pass
	
	def Toggle(self):
		self.Checked = not self.Checked
	
	def FieldText(self, selected):
		text = self.Property + ":"
		text = text.ljust(self.MaxPropertyLength)
		
		## If selected add a check mark
		if self.Checked: ## ☑
			text += "Yes" ## "☒"
		else:
			text += "No" ## "☐"
		
		## If selected add a check mark
		if selected:
			text += "✓"
		
		return text
	
	def AllText(self, selected):
		text = self.FieldText(selected)
		
		desc = " " + self.Description
		
		text += desc.rjust(len(desc) + self.MaxLength() - len(text))
		
		return text
	
	def MaxLength(self):
		return self.MaxPropertyLength + self.MaxValueLength + 1 ## Extra check mark character

class ComboBox:
	def __init__(self, property, values, default=0, description=""):
		## Reference the property
		self.Property = property
		
		## Reference the values
		self.Values = values
		
		## Reference the check and set the default
		self.SelectedIndex = default
		
		## Reference the description
		self.Description = description
		
		## Reference the max property length
		self.MaxPropertyLength = 20 + 1 ## Extra colon characters
		
		## Reference the max value length
		self.MaxValueLength = 12
		
	def __del__(self):
		pass
	
	def Select(self, index):
		if index > len(self.Values) - 1: return
		
		if index < 0: return
		
		self.SelectedIndex = index
	
	def Next(self, amount):
		self.Select(self.SelectedIndex + amount)
	
	def Previous(self, amount):
		self.Select(self.SelectedIndex - amount)
	
	def FieldText(self, selected):
		text = self.Property + ":"
		text = text.ljust(self.MaxPropertyLength)
		
		## If selected add a check mark
		#if self.Checked: ## ☑
		#	text += "Yes" ## "☒"
		#else:
		#	text += "No" ## "☐"
		
		## Add the selected item
		text += self.Values[self.SelectedIndex]
		
		## Add arrows
		if self.SelectedIndex > 0:
			text += "◂"
		if self.SelectedIndex < len(self.Values) - 1:
			text += "▸"
		
		## If selected add a check mark
		if selected:
			text += "✓"
			
		
		return text
	
	def AllText(self, selected):
		text = self.FieldText(selected)
		
		desc = " " + self.Description
		
		text += desc.rjust(len(desc) + self.MaxLength() - len(text))
		
		return text
	
	def MaxLength(self):
		return self.MaxPropertyLength + self.MaxValueLength + 1 ## Extra check mark character


class VerticalMenu(Menu):
	def __init__(self, itemList, message=None):
		Menu.__init__(self, itemList, message)
		
		## Make an instance of a Key Preset with the chosen Key Codes
		self.textInput = TextInput([KeyCodes.UP, KeyCodes.DOWN, KeyCodes.LEFT, KeyCodes.RIGHT, KeyCodes.ENTER, KeyCodes.TAB])
		
		## Reference the max length
		#self.MaxLength = self.__MaxLength()
		
	def __call__(self, hints):
		"""Creates an interactive select menu for the user. The user's choice is selected with up/down/left/right arrow keys and confirmed with the enter/return key.

		Returns:
			Option (from list) selected by user.
		"""
		
		return self.__DisplayMenu(hints)
	
	def Add(self, item):
		self.itemList.append(item)
	
	def AddText(self, text):
		if type(text) is string:
			self.itemList.append(text)
	
	def AddInput(self, property, default, description):
		self.itemList.append(Input(property, default, description))
	
	def __DisplayMenu(self, hints):
		## Declare the selected input index
		selectedIndex = self.__NextIndex(-1)
		
		## Infinite loop broken by return
		while True:
			for idx, item in enumerate(self.itemList):
				## Display if its a text
				text = ""
				if isinstance(item, str):
					text += item
				elif isinstance(item, (Input, CheckBox, ComboBox)):
					text += item.AllText(selectedIndex == idx)
				
				print(text)
			
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
				key_pressed = self.textInput.Input()
				
				## Check if a character was inputed
				chr = self.textInput.InputChr
				
				## Reference the item
				item = self.itemList[selectedIndex]
				
				## Change input text if character was inputed
				if key_pressed == -1:
					if isinstance(item, Input):
						item.Change(chr)
				elif key_pressed == 0:
					selectedIndex = self.__PreviousIndex(selectedIndex)
				elif key_pressed == 1:
					selectedIndex = self.__NextIndex(selectedIndex)
				elif key_pressed == 2:
					if isinstance(item, ComboBox):
						item.Previous(1)
				elif key_pressed == 3:
					if isinstance(item, ComboBox):
						item.Next(1)
				elif key_pressed == 4:
					if isinstance(item, Input):
						pass #item.Change(chr)
					elif isinstance(item, CheckBox):
						item.Toggle()
				elif key_pressed == 5:
					## Clear the text
					self.Clear(hints)
					
					Display.ClearPreviousLine()
					
					## Call the last option
					return True
			
			## Clear the text
			self.Clear(hints)
			
			## Return if anything was selected
			if opt:
				Display.ClearPreviousLine()
				return opt
	
	def __NextIndex(self, selectedIndex):
		## Reference the next id
		nextIdx = -1
		
		## Check for the next index and set if found
		for idx in range(selectedIndex + 1, len(self.itemList)):
			item = self.itemList[idx]
			if isinstance(item, (Input, CheckBox, ComboBox)):
				nextIdx = idx
				break
		
		## If next index not found, try from the beginning
		if nextIdx == -1:
			nextIdx = self.__NextIndex(nextIdx)
		
		## Return the next index
		return nextIdx
	
	def __PreviousIndex(self, selectedIndex):
		## Reference the previous id
		previousIdx = -1
		
		## Check for the previous index and set if found
		for idx in range(selectedIndex - 1, -2, -1):
			item = self.itemList[idx]
			if isinstance(item, (Input, CheckBox, ComboBox)): 
				previousIdx = idx
				break
			
		## If previous index not found, try from the ending
		if previousIdx == -1:
			previousIdx = self.__PreviousIndex(len(self.itemList) - 1)
		
		## Return the previous index
		return previousIdx
	
	def __MaxLength(self):
		## Reference the max length
		maxLength = 0
		
		## Iterate all the items in item list
		for idx, item in enumerate(self.itemList):
			## Check if its an Input item
			if isinstance(item, (Input, CheckBox, ComboBox)):
				## Get the current item length
				curLength = len(item.FieldText(False))
				
				## If the current item length is greater than the max, set it as the max
				if curLength > maxLength:
					maxLength = curLength
		
		## Return the length
		return maxLength
	
	def Clear(self, hints):
		## Clear hints
		if hints: self._ClearHints()
		
		## Clear the previously displayed options
		Display.ClearPreviousLine()
		
		for i in range(0, len(self.itemList)):
			Display.ClearPreviousLine()

