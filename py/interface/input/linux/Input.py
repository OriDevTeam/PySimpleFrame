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

## Library imports ##
import tty, termios, fcntl

## Application imports ##
from interface.input import KeyCodes

class Input:
	def _getch():
		# Read single key press from user
		
		## Get STDIN file descriptor
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setcbreak(sys.stdin.fileno())
			ch = ""
			for _ in range(3): # Reading maximum 3 bytes
				ch += sys.stdin.read(1)
				
				if not ch.startswith('\x1b'):
					# Exit if no escape sequence (used by arrow keys)
					break
		except:
			return None
			# nothing
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch

	def smt():
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		old_flags = fcntl.fcntl(fd, fcntl.F_GETFL)
		try:
			tty.setraw(fd)
			fcntl.fcntl(fd, fcntl.F_SETFL, old_flags | os.O_NONBLOCK)
			return sys.stdin.buffer.raw.read(1)
		finally:
			fcntl.fcntl(fd, fcntl.F_SETFL, old_flags)
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

	def GetInput():
		# Convert keycode input into commands
		k = None
		
		while(1):
			k = _getch()
			
			if k!="":
				break
		
		return k
