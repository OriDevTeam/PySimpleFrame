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
import os
import time

## Library imports ##
from colorama import Fore, Back, Style

## Application imports ##
from pysimpleframe.interface.display.controls import ProgressBar
from pysimpleframe.interface.display import Display


class ProgressReporter:
	def __init__(self, titleList, maxProgress):
		## Create the current index
		self.CurrentIndex = 0
		
		## Reference the maximum progress
		self.maxProgress = maxProgress
		
		## Reference the title list
		self.titleList = titleList
		
		## Create the progress List
		self.progressList = []
	
	def __del__(self):
		self.title = ""
		self.currentProgress = 0
		self.maxProgress = 0
	
	def Display(self):
		## Display the title
		self.__DisplayTitle()
		
		## Display the progress
		self.__DisplayProgress(action)
		
		## Display the progress actions
		self.__DisplayProgressList(action)
		
		## Increment the current progress index
		self.currentProgress += 1
		
		## Display the progress bar
		self.__DisplayProgressBar()
	
	def AddProgress(self, progress):
		## Append action to progress
		self.progressList.append(action)
	
	def AddTitle(self, title):
		self.titleList.append(title)
	
	def __DisplayTitle(self):
		Display.Print(Fore.GREEN + '############################################################')
		
		for title in self.titleList:
			Display.Print(Fore.GREEN + '##' + Fore.YELLOW + ' %s' % title)
		
		Display.Print(Fore.GREEN + '############################################################')
	
	def __DisplayProgressList(self, action):
		for idx in range(len(self.progressList)):
			if not idx + 1 == self.currentProgress:
				Display.Print(Fore.YELLOW + '## %s' % self.progressList[idx])
			else:
				Display.Print(Fore.GREEN + '## %s' % self.progressList[idx])
		
		Display.Print(Fore.GREEN + '############################################################')
	
	def __DisplayProgress(self, action):
		Display.Print(Fore.GREEN + '##' + Fore.YELLOW + ' %s (%s of %s)' % (action, self.currentProgress, self.maxProgress))
		Display.Print(Fore.GREEN + '############################################################')
	
	def __DisplayProgressBar(self):
		ProgressBar.CreateProgressBar(self.currentProgress, self.maxProgress, prefix = 'Progress:', suffix = 'Complete', length = 20)
		

