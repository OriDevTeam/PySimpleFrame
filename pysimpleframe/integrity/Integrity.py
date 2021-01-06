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
import re

## Library imports ##

## Application imports ##


class Integrity:
	def IsValidEmail(email):
		regex = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
		return re.search(regex, email)
	
	def IsValidInt(s):
		s = str(s)
		if s[0] in ('-', '+'):
			return s[1:].isdigit()
		return s.isdigit()  
	
	def IsValidString(object):
		return isinstance(object, str) 
	
	def IsValidPassword(string):
		return False
	