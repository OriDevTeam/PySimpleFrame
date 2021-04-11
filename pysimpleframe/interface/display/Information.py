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
import os
import subprocess
import platform
import io

## Library imports ##
from colorama import init, Fore, Back, Style

## Application imports ##


def DisplayDaemonInformation():
	## Display the title, python and system name
	DisplayTitle()
	DisplayPythonName()
	DisplaySystemName()

def DisplayStartInformation():	
	## Display the python and system name
	DisplayPythonName()
	DisplaySystemName()

def DisplayEndInformation():
	print("")
	print(Fore.YELLOW + "👋" + Fore.GREEN + "Goodbye!")
	print("")
	
def DisplayTitle(titlePath=''):
	## Try to read the text from the given file
	try:
		## Open the file in read mode ## TODO: read mode open
		f = open(titlePath)
		
		## Print the read text
		print(f.read().encode().decode('unicode_escape'))

	except (IOError, OSError) as e:
		print(f"Could not display title from {titlePath}:{e}")

def DisplayPythonName():
	## Get Python information and prettify it
	info = Fore.YELLOW + "Python: " + Fore.GREEN + "%s" % (platform.python_version())
	
	## Print the OS info
	print(info)

def DisplaySystemName():
	## Get Environment information and pretify it
	info = Fore.YELLOW + "Env: " + Fore.GREEN + "%s - %s " % (platform.system(), platform.release())
	
	## Print the Environment info
	print(info)
