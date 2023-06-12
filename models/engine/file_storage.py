#!/usr/bin/python3
"""File stoarage module"""
import json
import os


class FileStorage:
    """The class that serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    # private class attributes
    __file_path = 'db.json'
    __objects = {}

    # public instance methods
    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with the key `<obj class name>.id`"""
        key = F'{type(obj).__name__}.{obj.id}'
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file path(__file_path)"""
        with open(FileStorage.__file_path, 'w') as file:
            d = {}
            [d.update({k: v.to_dict()}) for k, v in self.all().items()]
            json.dump(d, file)

    def reload(self):
        """Deseialize the JSONfile to __objects(only if __file_path exists)"""
        from models.base_model import BaseModel
        classes = {'BaseModel': BaseModel}
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                jsonstring = json.load(file)
                for k, v in jsonstring.items():
                    self.all()[k] = classes[v['__class__']](**v)
