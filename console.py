#!/usr/bin/python3
"""Console module"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class
    """

    prompt = "(hbnb) "

    l_classes = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the console using Ctrl+D
        """
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
            return
        new_instance = eval(args[0])()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        obj_key = args[0] + "." + args[1]
        if obj_key in objs:
            print(objs[obj_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        obj_key = args[0] + "." + args[1]
        if obj_key in objs:
            del objs[obj_key]
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
        """
        Updates an instance based on the class name and id by adding or updating attribute
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        obj_key = args[0] + "." + args[1]
        if obj_key not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(objs[obj_key], args[2], args[3])
        objs[obj_key].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
