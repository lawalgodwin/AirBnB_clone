#!/usr/bin/python3
"""Console app (Front end for the admin users)"""

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """The class that handles all command from a user"""
    prompt = '(hbnb) '

    def do_hello(self):
        """Introduction to the app"""
        print('Documented commands (type help <topic>):')
        print('========================================')

    def postloop(self):
        """Called after the command loop has exited"""
        print('Goodbye...')

    def help_quit(self):
        """How to exit the program"""
        print('Quit command to exit the program')

    def do_EOF(self, line):
        """End of File"""
        return True

    def do_quit(self, line):
        """Exit the program"""
        print('Exiting...')
        sys.exit()

    def emptyline(self):
        """Called when when an empty line is entered"""
        print('Please enter a command or type "help" for assistance')


if __name__ == '__main__':
    try:
        HBNBCommand().cmdloop()
    except KeyboardInterrupt:
        print('Program interrupted')
