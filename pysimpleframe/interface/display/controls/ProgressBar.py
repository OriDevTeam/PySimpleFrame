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
import os
import time

## Library imports ##
from colorama import Fore, Back, Style

## Application imports ##


def CreateProgressBar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
	"""
	Creates a progress bar with the given details
	
	:param iteration: Current iteration
	:type iteration: int
	
	:param total: Total iterations
	:type total: int
	
	:param prefix: Prefix string
	:type prefix: string
	
	:param suffix: Suffix string
	:type suffix: string
	
	:param decimals: Positive number of decimals in percent complete
	:type decimals: int
	
	:param length: Character length of bar
	:type length: int
	
	:param fill: Bar fill character
	:type fill: string
	
	:param endingCharacter: Ending character
	:type endingCharacter: char
	
	:returns: Progress Bar with the given details
	:rtype: string
	
	"""
	
	percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
	filledLength = int(length * iteration // total)
	bar = fill * filledLength + '-' * (length - filledLength)
	
	progressBar = f'\r{prefix} |{bar}| {percent}% {suffix}' #, end = printEnd
	
	return progressBar
	
