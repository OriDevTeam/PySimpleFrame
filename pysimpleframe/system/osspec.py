#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Name: Operative System Specifications Module\n
   Description: Checks information about the Operative System and specifications
"""

"""PySimpleFrame
   Author: Miguel Silva
   License: Check LICENSE file
"""

## System imports ##
import platform
from enum import Enum, IntEnum, unique

## Library imports ##


## Application imports ##


@unique
class OperativeSystemBase(Enum):
	Windows = "Windows",
	Linux 	= "Linux",
	Darwin 	= "Darwin"
	

class OperativeSystem(object):
	@staticmethod
	def IsWindows():
		return platform.system() == OperativeSystemBase.Windows
	
	@staticmethod
	def IsLinux():
		return platform.system() == OperativeSystemBase.Linux
	
	@staticmethod
	def IsDarwin():
		return platform.system() == OperativeSystemBase.Darwin

