#!/usr/bin/python3
""" Command line interpreter for the program """
import cmd
import shlex
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Class attributes """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the command interpreter."""
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter at end-of-file (Ctrl+D)."""
        print("")  # Print a newline
        return True

    def emptyline(self):
        """Do nothing on empty input."""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel and save it to JSON file."""
        # Implementation for creating instances goes here

    def do_show(self, arg):
        """Show the string representation of an instance."""
        # Implementation for showing instances goes here

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