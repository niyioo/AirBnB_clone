#!/usr/bin/python3
"""Console module"""

import cmd
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = "(hbnb) "

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
        """Create a new instance of BaseModel and save it to JSON file."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        new_instance = globals()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Show the string representation of an instance."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instances = storage.all()  # Replace with your actual storage
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
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instances = storage.all()  # Replace with your actual storage
        instance_id = args[1]
        key = class_name + "." + instance_id
        if key in instances:
            instances.pop(key)
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name
        """
        args = shlex.split(arg)
        objs = storage.all()
        obj_list = []
        if not arg:
            for obj_key in objs:
                obj_list.append(str(objs[obj_key]))
        elif args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
            return
        else:
            for obj_key in objs:
                if obj_key.split('.')[0] == args[0]:
                    obj_list.append(str(objs[obj_key]))
        print(obj_list)

    def do_update(self, arg):
        """Update an instance based on class name and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instances = storage.all()  # Replace with your actual storage
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
