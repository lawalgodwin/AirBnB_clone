#!/usr/bin/python3
"""Console app (Front end for the admin users)"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
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
            print("** class name missing **")
        elif len(line.split(' ')) < 2:
            print('** instance id missing **')
        elif line.split(' ')[0] not in self.__classes.keys():
            print("** class doesn't exist **")
        else:
            modelName, ID = line.split(' ')
            key = f'{modelName}.{ID}'
            if key not in self.__allObjects.keys():
                print(f"** no instance found **")
            else:
                obj = self.__allObjects[key]
                print(obj)

    def do_destroy(self, line):
        """Deletes an object with the given ID"""
        if line == "" or line is None:
            print('** class name missing **')
        elif len(line.split(' ')) < 2:
            print("** instance id missing **")
        elif line.split(' ')[0] not in self.__classes.keys():
            print("** class doesn't exist **")
        else:
            modelName, ID = line.split(' ')
            key = f'{modelName}.{ID}'
            try:
                del storage.all()[key]
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all objects of the type(line)"""
        if line not in self.__classes.keys():
            print("** class doesn't exist **")
        else:
            filteredObjects = {}
            objects = self.__allObjects
            for k, v in objects.items():
                modelName = k.split('.')[0]
                if modelName == line:
                    filteredObjects.update({k: v})
            storedObjects = [str(v) for k, v in filteredObjects.items()]
            print(storedObjects)

    def do_update(self, line):
        """Update an object specified by the given ID"""
        try:
            modelName = line.split()[0]
        except IndexError:
            return print("** class name missing **")

        if modelName not in self.__classes.keys():
            return print("** class doesn't exist **")

        try:
            ID = line.split()[1]
        except IndexError:
            return print("** instance id missing **")

        key = f'{modelName}.{ID}'
        if not storage.all().get(key):
            return print("** no instance found **")

        try:
            attr = line.split()[2]
        except IndexError:
            return print("** attribute name missing **")

        if attr in ['id', 'updated_at', 'created_at']:
            return False

        try:
            attrValue = line.split()[3]
        except IndexError:
            return print("** value missing **")

        data = {}

        if type(attr) is str:
            attrValue = str(attrValue.replace('"', '').replace("'", ''))
        elif type(attr) is float:
            attrValue = float(attrValue)
        else:
            attrValue = int(attrValue)
        # prepare the data to make changes with
        d = {attr: attrValue}
        data.update(storage.all()[key].to_dict())
        data.update(d)
        """ update the data """
        dataToBeChanged = storage.all()[key]
        # check if data needs to be updated
        # if dataToBeChanged.to_dict() == data:
        #  return
        # make changes and save
        # storage.all()[key] = self.__classes[modelName](**data)
        setattr(storage.all()[key], attr, attrValue)
        storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
