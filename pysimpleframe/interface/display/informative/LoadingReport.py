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
import sys
import time

## Library imports ##
from halo import Halo
from log_symbols import LogSymbols #Enum

## Application imports ##
from pysimpleframe.interface.display import Display

class MultiLoadingReport:
	def __init__(self):
		self.spinnerList = []
	
	def __del__(self):
		pass
	
	def __call__(self, message, postMessage):
		## Check if theres any messages in the spinner list
		if len(self.spinnerList) > 0:
			## Reference the message from the spinner list
			self.spinner = self.spinnerList[len(self.spinnerList) - 1]
			
			## Set the message as successful with the post message
			self.spinner[0].succeed(self.spinner[1])
		
		## Create the spinner message
		spinner = Halo(text=message, spinner='dots')
		
		## Display the message
		spinner.start()
		
		## Add the message to the spinner list
		self.spinnerList.append([spinner, postMessage])
		
		## Change the count
		Display.Change(1)
		
		
	def fail(self, message):
		## Set the message spinner as unsuccessful
		self.spinnerList[len(self.spinnerList) - 1][0].fail(message)
	
	def succeed(self):
		## Reference the last message from the spinner list
		self.spinner = self.spinnerList[len(self.spinnerList) - 1]
		self.spinner[0].succeed(self.spinner[1])
		
		## Change the count
		Display.Change(1)
	
	def stop(self, clearTime=0):
		## Set last message as successful
		self.succeed()
		
		## Wait for some time before clearing
		time.sleep(clearTime)
		
		## Clear the display
		Display.ClearDisplay()
		
		

class LoadingReport:
	def __init__(self, message):
		## Show the message
		self.spinner = Halo(text=message, spinner='dots')
		self.spinner.start()
	
	def __del__(self):
		self.spinner.stop()
	
	def __call__(self, message):
		pass
