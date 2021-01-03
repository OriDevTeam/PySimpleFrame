#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""PySimpleFrame
   Name: TOFILL
   Author: Miguel Silva
   Description: TOFILL
   License: CC BY-SA 4.0 - Check LICENSE file
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
	
def DisplayTitle():
	## Display the title
	DisplayTitle()

def DisplayStartInformation():	
	## Display the python and system name
	DisplayPythonName()
	DisplaySystemName()

def DisplayEndInformation():
	print("")
	print(Fore.YELLOW + "👋" + Fore.GREEN + "Goodbye!")
	print("")
	
def DisplayTitle():
	## Declare the path of the file
	titlePath = r'app/interface/page/titles/title.txt'
	
	## Try to read the text from the given file
	try:
		## Open the file in read mode
		f = open(titlePath)
		
		## Print the read text
		print(f.read().encode().decode('unicode_escape'))

	except (IOError, OSError) as e:
		print("Could not display title")

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
