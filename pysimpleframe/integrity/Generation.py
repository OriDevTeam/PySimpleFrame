#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""PySimpleFrame
   Name: TOFILL
   Author: Miguel Silva
   Description: TOFILL
   License: CC BY-SA 4.0 - Check LICENSE file
"""

## System imports ##
import secrets
import random
from datetime import datetime

## Library imports ##

## Application imports ##


class Generation:
	def get_random_alphanumeric_string(length):
		letters_and_digits = string.ascii_letters + string.digits
		result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
		
		return result_str
	
	def get_secure_random_string(length):
		secure_str = ''.join((secrets.choice(string.ascii_letters) for i in range(length)))
		
		return secure_str
	
	def DateTimeToInt(date):
		# Converting a to string in the desired format (YYYYMMDD) using strftime
		# and then to int.
		date = int(date.strftime('%Y%m%d'))
		
		return date
	
	def IntToDateTime(timestamp):
		date = datetime.fromtimestamp(timestamp / 1e3)
		
		return date
