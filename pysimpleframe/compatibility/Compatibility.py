#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Name: Compatibility Module\n
   Description: Performs compatibility checks for Python and OS compatibility
"""

"""PySimpleFrame
   Author: Miguel Silva
   License: Check LICENSE file
"""

## System imports ##
import os
import platform
import re
import importlib
import subprocess
import sys
import pip

## Library imports ##
from packaging import version
from colorama import Fore, Back, Style

## Application imports ##


## Minimum Python Version
MIN_VERSION = "3.8"
	

def IsPythonCompatible():
	"""Check if the current Python execution meets the minimum required version
	
	:returns compatible bool: Tells if its Python compatible
	"""
	
	## Get Python version
	curVersion = platform.python_version()
	
	return version.parse(curVersion) > version.parse(MIN_VERSION)

def IsLibrariesCompatible():
	"""
	"""
	
	## Get OS information
	system = platform.system()
	release = platform.release()
	
	## Create the known OS list
	sysList = {
		"MSYS_NT*" : Compatibility.IsMSYSCompatible,
        "Windows" : Compatibility.IsWindowsCompatible,
        "Linux" : Compatibility.IsLinuxCompatible,
		"CYGWIN" : Compatibility.IsCYGWINCompatible,
		"FreeBSD" : Compatibility.IsFBSDCompatible,
        "Darwin" : Compatibility.IsMacOSXCompatible,
    }
	
	## Get an OS from the known list
	for key, value in sysList.items():
		if re.search(key, system):
			osFunc = value
	
	## Check if we detected any known OS 
	if not osFunc:
		print("Invalid Operative System, please review")
		return
	
	## Execute the compatibility checking function
	osFunc()

class Compatibility:
	def IsMSYSCompatible():
		## Declare the install command
		installCommand = "pacman -S"
		
		## Check if its compatible
		Compatibility.IsOSCompatible(installCommand)
		
	def IsWindowsCompatible():
		print("Its Win32")
		
		## Declare the install command
		installCommand = "pacman -S"
		
		## Check if its compatible
		Compatibility.IsOSCompatible(installCommand)
	
	def IsLinuxCompatible():
		print("Its Linux")
		
		## Declare the install command
		installCommand = "apt-get install"
		
		## Check if its compatible
		Compatibility.IsOSCompatible(installCommand)
	
	def IsFBSDCompatible():
		print("Its FreeBSD")
		
		## Declare the install command
		installCommand = "pkg install"
		
		## Check if its compatible
		Compatibility.IsOSCompatible(installCommand)
	
	def IsCYGWINCompatible():
		print("Its CygWin")
		
		## Declare the install command
		installCommand = "apt-cyg install"
		
		## Check if its compatible
		Compatibility.IsOSCompatible(installCommand)
	
	def IsMacOSXCompatible():
		print("Its MacOS")
		
		## Declare the install command
		installCommand = "apt-get install"
		
		## Check if its compatible
		Compatibility.IsOSCompatible(installCommand)
	
	def IsOSCompatible(installCommand):		
		## Get the necessary libraries
		installList = []
		
		## Check if each lib listed is installed
		for lib in installList:
			
			## Get if the spec module exists
			spec = importlib.util.find_spec(lib)
			
			## Install if it doesn't exist
			if spec is None:
				os.system("%s %s" % (installCommand, lib))
		
class OperativeSystem:
	def IsWindows():
		return "Windows" in platform.system()
	
	def IsLinux():
		return "Linux" in platform.system()
