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

## Library imports ##
from colorama import Fore, Back, Style

## Application imports ##
from pysimpleframe.interface.page.PageControl import PageControl

from pysimpleframe.interface.display import Display

from pysimpleframe.interface.display.menu import SelectMenu
from pysimpleframe.interface.display.menu import MultiSelectMenu


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
		
