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
from enum import Enum, IntEnum, unique

## Library imports ##

## Application imports ##
from pysimpleframe.compatibility.Compatibility import OperativeSystem

## Import input according to detected OS
if OperativeSystem.IsWindows():
	from pysimpleframe.interface.input.windows.KeyCodes import KeyCodes
else:
	from pysimpleframe.interface.input.linux.KeyCodes import KeyCodes

