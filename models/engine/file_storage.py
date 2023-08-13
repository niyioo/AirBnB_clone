#!/usr/bin/python3
""" File storage for the airbnb """
import json
from models.base_model import BaseModel


class FileStorage:
    """ file storage class attributes """
    __file_path = "file.json"
    __objects = {}
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def all(self, cls=None):
        """Return the dictionary __objects."""
        if cls is None:
            return self.__objects
        else:
            filtered_objs = {
                key: obj for key, obj in self.__objects.items()
                if cls == key.split('.')[0]
            }
            return filtered_objs

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        data = {}

        for key, obj in FileStorage.__objects.items():
            data[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w") as file:
            json.dump(data, file)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = value["__class__"]
                    del value["__class__"]
                    if class_name in self.classes:
                        obj = self.classes[class_name](**value)
                        self.new(obj)
        except FileNotFoundError:
            pass
    
    def count(self, cls=None):
        """Count the number of instances of a class."""
        if cls:
            return len(self.all(cls))
        return len(self.all())