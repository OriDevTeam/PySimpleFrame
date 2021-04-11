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

import sys
import tty, termios, fcntl
import os

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

while True:
	k = smt()
	
	if k: print(k)