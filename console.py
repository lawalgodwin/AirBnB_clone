#!/usr/bin/python3
"""Console app (Front end for the admin users)"""

import ast
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import re
from models import storage
import json
import sys


class HBNBCommand(cmd.Cmd):
    """The class that handles all command from a user"""
    __classes = {
                    'BaseModel': BaseModel,
                    'User': User,
                    'Place': Place,
                    'State': State,
                    'City': City,
                    'Amenity': Amenity,
                    'Review': Review
    }
    __allObjects = storage.all()
    prompt = '(hbnb) '

    def default(self, line):
        """Override command execution based on user input"""
        self.precmd(line)

    def precmd(self, line):
        """Preprocess user input before using it for computation"""
        if "." in line:
            result = re.search(r"^(\w+)\.(\w+)(\(.*\))$", line)
            if result:
                resource = result.group(1)
                command = result.group(2)
                ID = ''
                _cmd = ''
                args = result.group(3).strip('(').strip(')')
                # test for occurence of a dictionary
                dictfound = re.search(r'(\{.*\})', args)
                if dictfound and command == "update":
                    data = (dictfound.group(1).replace(':', ''))
                    data = str(data).strip('{').strip('}')
                    field_and_value = str(data).replace('"', '')
                    field_and_value = str(field_and_value).replace("'", '')
                    field_and_value = str(field_and_value).replace(',', '')
                    ID = str(args.split(',')[0]).replace('"', '')
                    _cmd = (
                            command + ' '
                            + resource + ' '
                            + ID + ' '
                            + field_and_value
                    )
                    return _cmd
                else:
                    args = args.replace(',', '')
                    args = args.replace('"', '').replace("'", '')
                    _cmd = command + ' ' + resource + ' ' + args
                # self.onecmd(userCmd)
                    return _cmd

        return line.strip()

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
        if line == "" or line is None:
            return (print("** class name missing **"))
        modelName = line
        if modelName in self.__classes.keys():
            obj = self.__classes[modelName]()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """show an object with a particular ID"""
        if line == "" or line is None:
            return print("** class name missing **")
        line = re.findall(r'"[^"]+"|\S+', line)
        if line[0] not in self.__classes.keys():
            print("** class doesn't exist **")
        elif len(line) < 2:
            print('** instance id missing **')
        else:
            modelName, ID = line
            key = f'{modelName}.{ID}'
            if key not in self.__allObjects.keys():
                print(f"** no instance found **")
            else:
                obj = self.__allObjects[key]
                print(obj)

    def do_destroy(self, line):
        """Deletes an object with the given ID"""
        if line == "" or line is None:
            return print('** class name missing **')
        line = re.findall(r'"[^"]+"|\S+', line)
        if len(line) < 2:
            print("** instance id missing **")
        elif line[0] not in self.__classes.keys():
            print("** class doesn't exist **")
        else:
            modelName, ID = line
            key = f'{modelName}.{ID}'
            try:
                del storage.all()[key]
                storage.save()
            except KeyError:
                return print("** no instance found **")

    def do_all(self, line):
        """Prints all objects of the type(line)"""
        className = line
        if className not in self.__classes.keys():
            return print("** class doesn't exist **")
        if '.' in line:
            className, command = line.split('.')
        else:
            className = line

        filteredObjects = {}
        objects = self.__allObjects
        for k, v in objects.items():
            modelName = k.split('.')[0]
            if modelName == className:
                filteredObjects.update({k: v})
        storedObjects = [str(v) for k, v in filteredObjects.items()]
        print(storedObjects)

    def do_update(self, line):
        """Update an object specified by the given ID"""
        try:
            modelName = re.findall(r'"[^"]+"|\S+', line)[0]
        except IndexError:
            return print("** class name missing **")

        if modelName not in self.__classes.keys():
            return print("** class doesn't exist **")

        try:
            ID = re.findall(r'"[^"]+"|\S+', line)[1]
        except IndexError:
            return print("** instance id missing **")

        key = f'{modelName}.{ID}'
        if not storage.all().get(key):
            return print("** no instance found **")

        try:
            attr = re.findall(r'"[^"]+"|\S+', line)[2]
        except IndexError:
            return print("** attribute name missing **")

        if attr in ['id', 'updated_at', 'created_at']:
            return False

        try:
            attrValue = re.findall(r'"[^"]+"|\S+', line)[3]
        except IndexError:
            return print("** value missing **")

        attrValue = str(attrValue).replace(',', '')

        """ update the data """
        instance = eval(modelName)()
        if hasattr(instance, attr):
            variable = getattr(instance, attr)
            castType = type(variable).__name__
            setattr(storage.all()[key], attr, eval(castType)(attrValue))
            storage.all()[key].save()
        else:
            setattr(storage.all()[key], attr, attrValue)
            storage.all()[key].save()

    def do_count(self, line):
        """Print the number of an object"""
        if line == "" or line is None:
            return print("** class name missing **")
        line = re.findall(r'"[^"]+"|\S+', line)
        if line[0] not in self.__classes.keys():
            print("** class doesn't exist **")
        else:
            objKeys = []
            for k in storage.all().keys():
                if k.startswith(line[0]):
                    objKeys.append(k)
            print(len(objKeys))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
