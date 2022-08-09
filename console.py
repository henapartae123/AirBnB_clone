#!/usr/bin/python3
"""Defines the HBNB console"""
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Do nothing when an empty line is executed"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()