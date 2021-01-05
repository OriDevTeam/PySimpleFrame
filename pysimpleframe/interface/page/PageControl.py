#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""PySimpleFrame
   Name: TOFILL
   Author: Miguel Silva
   Description: TOFILL
   License: Check LICENSE file
"""

## System imports ##

## Library imports ##
from colorama import Fore, Back, Style

## Application imports ##
from pysimpleframe.interface.display import Display


class PageControl(object):
	## Create the initialized state
	__initialized = False
	
	## Create the pages list
	Pages = []
	
	## Create the base display functions list
	DisplayFunctions = []
	
	@classmethod
	def Init(cls):
		## Return if already initialized
		if cls.__initialized: return
		
		## Add the page navigation label function
		cls.DisplayFunctions.append(cls.DisplayManagerNavigationLabel)
	
	@classmethod
	def AddBaseDisplay(cls, function):
		## Adds a function to display when base display is called
		if not function in cls.DisplayFunctions:
			cls.DisplayFunctions.append(function)
	
	@classmethod
	def DoBaseDisplay(cls):
		## Call all base display functions in the list
		for function in cls.DisplayFunctions:
			function()
	
	@classmethod
	def PreviousPage(cls):
		## Return the previous page if there is any
		if len(cls.Pages) >= 1: return cls.Pages[-1]
		
		return None
	
	@classmethod
	def Unregister(cls, page):
		## Remove the page from the list if exists
		if page in cls.Pages: cls.Pages.remove(page)
	
	@classmethod
	def UnregisterAll(cls):
		## Clear all the pages from the list
		cls.Pages = []
	
	@classmethod
	def Register(cls, page):
		## Register the page if doesn't exist
		if not page in cls.Pages: cls.Pages.append(page)
	
	@classmethod
	def DisplayManagerNavigationLabel(cls):
		## Display a empty navigation if empty pages list and return
		if len(cls.Pages) < 1:
			Display.Print("")
			return
		
		## Create the label
		label = Fore.YELLOW + "Navigation: " + Fore.WHITE
		
		## Reference the index
		idx = 0
		
		## Add each page name by succession
		for i in range(len(cls.Pages) - 1):
			label += cls.Pages[i].Name + " > "
		
		## Add the last page name with color
		label += Fore.GREEN + cls.Pages[len(cls.Pages) - 1].Name

		## Print the label
		Display.Print(label)
	