#!/usr/bin/python3
"""Console app (Front end for the admin users)"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
import json
import sys


class HBNBCommand(cmd.Cmd):
    """The class that handles all command from a user"""
    __classes = {'BaseModel': BaseModel, 'User': User}
    __allObjects = storage.all()
    prompt = '(hbnb) '

    def precmd(self, line):
        """Preprocess user input before using it for computation"""
        line = line.strip()
        return line

    def postloop(self):
        """Called after the command loop has exited"""
        print('\nGoodbye...')

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

    def do_create(self, line):
        """Save to Json file and print the ID"""
        if len(line) == 0:
            print('** class name missing **')
        elif line not in self.__classes.keys():
            print('** class doesn\'t exist **')
            return False
        else:
            new = eval("{}()".format(line))
            new.save()
            print(new.id)


if __name__ == '__main__':
    try:
        HBNBCommand().cmdloop()
    except KeyboardInterrupt:
        print('\nProgram interrupted')
