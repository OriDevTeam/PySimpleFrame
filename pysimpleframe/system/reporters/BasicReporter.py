#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Name: Reporter Script\n
   Description: Reports messages to registered subscribers (supports: threading)
"""

"""PySimpleFrame
   Author: Miguel Silva
   License: Check LICENSE file
"""

## System imports ##
from threading import Thread

## Library imports ##

## Application imports ##


class BasicReporter:
	def __init__(self, name):
		"""Initializes the reporter.
		
		Parameters:
			None
		
		Returns:
			None
		"""
		
		## Reference the name
		self.Name = name
		
		## Create a subscriber list
		self.SubscriberList = []
		
	def __del__(self):
		"""Deletes the reporter.
		
		Parameters:
			None
		
		Returns:
			None
		"""
		
		## Delete objects
		del self.SubscriberList
	
	def __iadd__(self, subscriberMethod, raiseError=False):
		"""Adds a subscriber method to the subscriber list
		
		Parameters:
			subscriberMethod [required](object): The subscriber method to call on report
			raiseError 		 [optional](boolean): 
			
		Returns:
			None
		"""
		
		## Check if subscriber method is callable, raise otherwise if specified
		if not hasattr(subscriberMethod, '__call__'):
			if raiseError: raise NotSubscriberError()
		
		## Add to subscribers if doesn't exist
		if not subscriberMethod in self.SubscriberList:
			self.SubscriberList.append(subscriberMethod)
		
		## Return self for setting
		return self
	
	def __isub__(self, subscriberMethod):
		## Remove from subscribers if does exist
		if subscriberMethod in self.SubscriberList:
			self.SubscriberList.remove(subscriberMethod)
		
		## Return self for setting
		return self
	
	def Report(self, *fargs):
		## Call all the subscribers in a thread and pass a message
		for subscriber in self.SubscriberList:
			## Create a thread to call pass the message
			thread = Thread(target=subscriber, args=(fargs))
			thread.name = f"{self.Name}-{subscriber}"
			
			## Start the thread
			thread.start()
	
	## TODO: Asynchronous Report support
	
