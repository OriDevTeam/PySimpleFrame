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
		
		self.maxProgress = maxProgress
		
		## Reference the title list
		self.titleList = titleList
		
		## Create the progress List
		self.progressList = []
	
	def __del__(self):
		self.title = ""
		self.currentProgress = 0
		self.maxProgress = 0
	
	def Display(self, action):
		self.__DisplayTitle()
		self.__DisplayProgress(action)
		self.__DisplayProgressList(action)
		
		self.progressList.append(action)
		self.currentProgress += 1
		
		
		self.__DisplayProgressBar()
	
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
		print(Fore.GREEN + '##' + Fore.YELLOW + ' %s (%s of %s)' % (action, self.currentProgress, self.maxProgress))
		Display.Print(Fore.GREEN + '############################################################')
	
	def __DisplayProgressBar(self):
		ProgressBar.CreateProgressBar(self.currentProgress, self.maxProgress, prefix = 'Progress:', suffix = 'Complete', length = 20)
		

