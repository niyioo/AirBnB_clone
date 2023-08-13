#!/usr/bin/python3
"""Console module"""

import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = "(hbnb) "

    valid_classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the console using Ctrl+D"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Create a new instance of a class and save it to JSON file."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        new_instance = self.valid_classes[class_name](storage=storage)
        new_instance.save()
        print(new_instance.id)

    def __getattr__(self, attr):
        """
        Handle dynamic attribute access for class.all() syntax
        """
        class_name = attr
        if class_name in self.valid_classes:
            return lambda x: self.do_all(f"{class_name}")
        raise AttributeError

    def default(self, line):
        """
        Handle dynamic attribute access for class.all() syntax in default case
        """
        args = line.split('.')
        if len(args) == 2:
            class_name = args[0]
            method_name = args[1]
            if class_name in self.valid_classes and method_name == "all()":
                self.do_all(f"{class_name}")
                return
        cmd.Cmd.default(self, line)

    def do_show(self, arg):
        """Show the string representation of an instance."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instances = storage.all()
        instance_id = args[1]
        key = class_name + "." + instance_id

        if key in instances:
            print(instances[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instances = storage.all()
        instance_id = args[1]
        key = class_name + "." + instance_id

        if key in instances:
            instances.pop(key)
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print string representation of all instances or of a specific class."""
        args = shlex.split(arg)
        if not args:
            instances_list = []
            for class_name in self.valid_classes:
                instances_list.extend(
                    [
                        str(instance)
                        for instance in storage.all(class_name).values()
                    ]
                )
            print(instances_list)
        else:
            class_name = args[0]
            if class_name not in self.valid_classes:
                print("** class doesn't exist **")
                return
            instances_list = [
                str(instance)
                for key, instance in storage.all(class_name).items()
            ]
            print(instances_list)

    def do_update(self, arg):
        """Update an instance based on class name and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instances = storage.all()
        instance_id = args[1]
        key = class_name + "." + instance_id

        if key not in instances:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attr_name = args[2]
        attr_value = args[3]
        instance = instances[key]
        setattr(instance, attr_name, attr_value)
        instance.save()

    def do_count(self, arg):
        """Retrieve the number of instances of a class."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        instances_count = storage.count(class_name)
        print(instances_count)

    def do_help(self, arg):
        """Display help information for commands."""
        if arg:
            cmd.Cmd.do_help(self, arg)
        else:
            topics = ", ".join(self.get_names())
            print("Documented commands (type help <topic>):")
            print("=" * 40)
            print(topics)
            print()

    def help_quit(self):
        print("Quit command to exit the program")

    def help_EOF(self):
        print("EOF command to exit the program (Ctrl+D)")

    def help_create(self):
        print("Create a new instance of BaseModel and save it to JSON file.")

    def help_show(self):
        print("Show the string representation of an instance.")

    def help_all(self):
        print("Print string representation of all instances of a class.")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
