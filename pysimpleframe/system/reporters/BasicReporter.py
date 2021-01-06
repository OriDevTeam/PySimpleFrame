#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""PySimpleFrame
   Name: Reporter Script
   Author: Miguel Silva
   Description: Reports messages to registered subscribers (async/non-async)
   License: Check LICENSE file
"""

## System imports ##

## Library imports ##

## Application imports ##


class Reporter:
	def __init__(self):
		"""Initializes the reporter.
		
		Parameters:
			None
		
		Returns:
			None
		"""
		
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
	
	def __isub__(self, subscriberMethod):
		## Remove from subscribers if does exist
		if subscriberMethod in self.SubscriberList:
			self.SubscriberList.remove(subscriberMethod)
	
	def Report(self, message, sync):	
		## Call all the subscribers and give a message
		for subscriber in self.SubscriberList:
			subscriber(message)
	
	
