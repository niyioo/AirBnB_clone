#!/usr/bin/python3
""" Parent class for Airbnb """
import uuid
from datetime import datetime


class BaseModel:
    """Defines attributes and methods for the base model."""
    def __init__(self, *args, **kwargs):
        """Initializes BaseModel instance."""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            
        else:
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, date_format)
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """Returns string representation of the instance."""
        class_name = "[" + self.__class__.__name__ + "]"
        attribute_dict = {
            k: v for (k, v) in self.__dict__.items() if v is not False
        }
        return class_name + " (" + self.id + ") " + str(attribute_dict)

    def save(self):
        """Updates updated_at with current datetime and saves to storage."""
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """Returns dictionary representation of the instance."""
        instance_dict = {}

        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                instance_dict[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if value is not None:
                    instance_dict[key] = value
        instance_dict['__class__'] = self.__class__.__name__

        return instance_dict
