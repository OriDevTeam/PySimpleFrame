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

## Library imports ##
from colorama import init, Fore, Back, Style

## Application imports ##
from pysimpleframe.interface.display.menu.SelectMenu import VerticalMenu
from pysimpleframe.interface.display import Display

from pysimpleframe.interface.input.KeyPreset import KeyPreset
from pysimpleframe.interface.input.KeyCodes import KeyCodes


class InteractiveKeys:
	def __init__(self, optionsList, showLabel=True):
		## Reference the options list
		self.optionsList = optionsList
		
		## Reference the show label option
		self.showLabel = showLabel
		
		## Append a the exit option
		self.optionsList.append([KeyCodes.COPYCANCEL, "Exit", lambda: False])

		## Get the keys for each option
		self.keyList = []
			
		## Make a Key Preset for the menu
		self.key_preset = KeyPreset(self.keyList)
		
		## Add each key in option
		for item in self.optionsList:
			if item: self.keyList.append(item[0])
	
	def __del__(self):
		del self.optionsList
		del self.keyList
		del self.key_preset
	
	def ShowLabel(self):		
		for idx in range(0, len(self.optionsList)):
			label = self.optionsList[idx]
			key = label[0]
			txt = label[1]
			
			if idx + 1 >= len(self.optionsList):
				Display.Print(Fore.YELLOW + txt + ": " + Fore.RED + key.keyname())
			else:
				Display.Print(Fore.YELLOW + txt + ": " + Fore.GREEN + key.keyname(), e=" | ")
	
	def __Input(self):
		## Hold the inputed option result
		inputing = True
		
		## Loop for the key menu
		while inputing:
			## Wait for the inputed index
			index = self.key_preset.Input()
			
			## Break if last item
			if index + 1 >= len(self.optionsList):
				break
			
			## Call the function in the list by index if valid and set the result
			if index > -1:
				inputing = self.optionsList[index][2]()
	
	def __call__(self):
		## Show the key labels if enabled
		if self.showLabel:
			self.ShowLabel()
		
		## Wait for input
		self.__Input()

	