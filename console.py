#!/usr/bin/python3
from models import storage
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
                storage.new(n_instance)
                storage.save()
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

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        save the change into the JSON file
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        try:
            class_ref = globals()[class_name]
        except KeyError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"

        try:
            instance = models.storage.all()[key]
            print(instance)
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints string representation of all instances
        based on the class name or all instances
        """
        args = arg.split()

        if not args:
            # is is all the instances
            x = models.storage.all()
            instance_list = [str(instance) for instance in x.values()]
            print(instance_list)
            return

        class_name = args[0]

        try:
            class_ref = globals()[class_name]
        except KeyError:
            print("** class doesn't exist **")
            return
        # x is all the instances
        x = models.storage.all()
        filtered_instances = [
                str(instance) for instance in x.values()
                if isinstance(instance, class_ref)
                ]
        print(filtered_instances)

    def do_pupdate(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attributes
        """
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        try:
            class_ref = globals()[class_name]
        except KeyError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"

        all_instances = models.storage.all()

        if key not in all_instances:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3]
        instance = all_instances[key]
        attribute_type = getattr(instance, attribute_name, None)

        if attribute_type is None:
            print("** attribute doesn't exist **")
            return

        # Update the attribute with the provided value
        setattr(instance, attribute_name, attribute_type(attribute_value))
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
