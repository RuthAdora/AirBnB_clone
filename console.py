import models
import cmd
import sys
from models.base_model import BaseModel
"""
module that contain an entry point
to the cmd interpreter
"""


class HBNBCommand(cmd.Cmd):
    "class that has an entry point to cmdline interpreter"
    prompt = ("(hbnb) ")

    def do_help(self, arg):
        "prints available commands"
        print("Available commands:")
        print("  exit/EOF: Exit the application")
        print("  help: Show this help message")

    def do_exit(self, arg):
        """Exit the application"""
        print("Exiting the application.")
        return True

    def do_EOF(self, arg):
        "exits the console using end of file signal"
        print()
        return True

    def do_quit(self, arg):
        "Exits application"
        return True

    def emptyline(self):
        "do not execute nothing"
        pass

    def do_create(self, arg):
        "creates an instance of class BaseModel"
        if not arg:
            print("** class name missing **")
        else:
            class_name = arg
            try:
                class_ref = globals()[class_name]
                n_instance = class_ref()
                n_instance.save()
                print(n_instance.id)
            except KeyError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        "prints string rep of an instance"
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        try:
            class_reference = globals()[class_name]
        except KeyError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        try:
            instance = models.storage.all()[key]
            print(instance)
        except KeyError:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
