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
import os
import re

## Library imports ##

## Application imports ##


class Integrity:
	def IsValidEmail(email):
		"""
		Checks if the given string contains the the necessary characters that
		constitutes an email
		
		:param email: email string to check if its valid
		:type email: string
		"""
		
		regex = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
		return re.search(regex, email)
	
	def IsValidInt(s):
		"""
		Checks if the given string is a valid intenger(checks if its digits)
		
		:param s: string to check if its valid
		:type s: string
		"""
		
		s = str(s)
		if s[0] in ('-', '+'):
			return s[1:].isdigit()
		return s.isdigit()  
	
	def IsValidString(object):
		"""
		Checks if the given object is of the instance string
		
		:param object: object to check if is string
		:type object: object
		"""
		return isinstance(object, str) 
	
	def IsValidPassword(string):
		"""
		Checks if the given string is a valid password string
		
		:param string: string to check if its a valid password
		:type string: object
		"""
		return False
	