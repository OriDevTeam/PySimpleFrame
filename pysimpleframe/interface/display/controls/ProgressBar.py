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
import time

## Library imports ##
from colorama import Fore, Back, Style

## Application imports ##


def CreateProgressBar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
	"""
	Call in a loop to create terminal progress bar
	@params:
		iteration   - Required  : current iteration (Int)
		total       - Required  : total iterations (Int)
		prefix      - Optional  : prefix string (Str)
		suffix      - Optional  : suffix string (Str)
		decimals    - Optional  : positive number of decimals in percent complete (Int)
		length      - Optional  : character length of bar (Int)
		fill        - Optional  : bar fill character (Str)
		#printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
	"""
	
	percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
	filledLength = int(length * iteration // total)
	bar = fill * filledLength + '-' * (length - filledLength)
	
	progressBar = f'\r{prefix} |{bar}| {percent}% {suffix}' #, end = printEnd
	
	return progressBar
	
	# Print New Line on Complete
	#if iteration == total: 
	#	print()
