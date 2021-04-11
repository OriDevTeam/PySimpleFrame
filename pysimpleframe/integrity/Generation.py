#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Name: Integrity Module\n
   Description: Handles the control of display of text in CLI
"""

"""PySimpleFrame
   Author: Miguel Silva
   License: Check LICENSE file
"""

## System imports ##
import secrets
import random
from datetime import datetime

## Library imports ##

## Application imports ##


class Generation:
	def get_random_alphanumeric_string(length):
		"""
		Generates a random alphanumeric string based on the given length
		
		:param length: The length of the string to generate
		:type length: int
		
		:return: A string with random ascii letters and digits
		:rtype: string
		"""
		
		letters_and_digits = string.ascii_letters + string.digits
		result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
		
		return result_str
	
	def get_secure_random_string(length):
		"""
		Generates a random alphanumeric string based on the given length
		
		:param length: The length of the string to generate
		:type length: int
		
		:return: A string with random ascii letters and digits
		:rtype: string
		"""
		
		secure_str = ''.join((secrets.choice(string.ascii_letters) for i in range(length)))
		
		return secure_str
	
	def DateTimeToInt(date):
		"""
		Converts a date to intenger by converting into a date string
		
		:param date: The date string to be converted
		:type date: datetime
		
		:return: The datetime converted into string then intenger
		:rtype: string
		"""
		
		## Converting a to string in the desired format (YYYYMMDD) using strftime
		## and then to int.
		date = int(date.strftime('%Y%m%d'))
		
		return date
	
	def IntToDateTime(timestamp):
		"""
		Converts a intenger to datetime by converting from a timestamp
		
		:param timestamp: The timestamp to convert into datetime
		:type timestamp: int
		
		:return: The intenger converted into datetime
		:rtype: string
		"""
		
		date = datetime.fromtimestamp(timestamp / 1e3)
		
		return date
