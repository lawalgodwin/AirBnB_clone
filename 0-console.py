#!/usr/bin/python3
"""This module serves as the entrypoint of command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command Interpreter class"""

    prompt = '(hbnb) '

    def do_create(self, line):
        """object creation handler"""
        print(line)

    def do_EOF(self, line):
        """Handle end_of_file character"""

        print()

        return True

    def do_quit(self, line):
        """Terminate program"""
        return True

    def emptyline(self):
        """Do nothing on pressing the ENTER key"""

        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
