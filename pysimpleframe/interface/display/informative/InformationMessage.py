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

## Application imports ##
from pysimpleframe.interface.input import Input


class Menu:
    """Interactive select menu.

    Attributes:
        opts (list of str): Options for the user to choose from.
    """
    opts = []

    def __init__(self, options, message=None):
        """Interactive select menu.

        Args:
            options (list of str): Options for the user to choose from.
            message (str, optional): Message to be displayed before showing options
        """
        self.opts = options
        if not message == None:
            print(message)
	
    def __call__(self):
        """Creates an interactive select menu for the user. The user's choice is selected with up/down/left/right arrow keys and confirmed with the enter/return key.

        Returns:
            Option (from list) selected by user.
        """
        selected = 0
        while True:
            # Infinite loop broken by return
            print("\r", end="")
            for ind, opt in enumerate(self.opts):
                if ind == selected:
                    print("\033[0;30;47m{}\033[0m".format(opt), end=" ")
                else:
                    print(opt, end=" ")
            sys.stdout.flush() # Forcing options to show (would be delayed until after keypress in Python 3)

            key_pressed = None
            while key_pressed == None:
                # Looping until valid key pressed
                key_pressed = Input._get_input()
                if (key_pressed == "next") and selected < (len(self.opts) - 1):
                    selected += 1
                elif (key_pressed == "prev") and selected > 0:
                    selected -= 1
                elif key_pressed == "select":
                    print("")
                    return self.opts[selected]

# Example Usage (exit menu):
# exit_menu = Menu(['Yes', 'No'], "Exit?")
# if exit_menu() == 'Yes':
#   sys.exit()