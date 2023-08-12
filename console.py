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
        cmd.Cmd.do_help(self, arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
