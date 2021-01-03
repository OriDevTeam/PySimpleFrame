#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""PySimpleFrame
   Name: TOFILL
   Author: Miguel Silva
   Description: TOFILL
   License: CC BY-SA 4.0 - Check LICENSE file
"""

## System imports ##

## Library imports ##
from colorama import Fore, Back, Style

## Application imports ##
from interface.display import Display

from interface.display.menu import SelectMenu
from interface.display.menu import MultiSelectMenu


class Page(object):
	def __init__(self, name, clear=True):		
		## Set the name of the page
		self.Name = name
		
		## Register the page in page control
		PageControl.Register(self)
		
		## Run the base before the page
		self.BaseRun(clear)
	
	def __del__(self):
		## Unregister the page from page control 
		PageControl.Unregister(self)
	
	def BaseRun(self, clear):
		## Clear the display if specified
		if clear: Display.ClearDisplay()
		
		## Execute the base display
		PageControl.DoBaseDisplay()
	
	def Refresh(self):
		self.BaseRun(True)
	
	def Next(self, nextMgr, clear=True):
		## Run the base operations
		self.BaseRun(clear)
		
		## Execute the next page
		nextMgr()
	
	def Previous(self):
		## Unregister the page
		PageControl.Unregister(self)
		
		## Run the base operations
		self.BaseRun(True)
		
		## Execute the last page if exists
		previousPage = PageControl.PreviousPage()
		
		## Call the previous page
		if previousPage: previousPage()
	
	def DisplayMenu(self, menuOptionsDict, next=True, question="What to manage?"):
		## Create a menu
		menu = SelectMenu.VerticalMenu(menuOptionsDict, question)
		
		## Display the menu and hold the picked option
		option = menu(False, True)[1]
		
		## Next the returned option if enabled
		if next: self.Next(option)
		
		## Return the picked option
		return option
	
	def DisplayMultiSelectMenu(self, menuOptionsDict):
		## Create a multi select menu
		menu = MultiSelectMenu.VerticalMenu(menuOptionsDict, "")
		
		## Display the menu and hold the picked option
		optionList = menu(False, True)
		
		## Return the picked options
		return optionList
		

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
	