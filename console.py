#!/usr/bin/python3
"""Defines the HBNB console"""
import cmd
import models



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
    
    def do_create(self, arg):
        """Create a new class instance and print its id"""
        if arg == "":
            print('** class name missing **')
            return
        try:
            model = models.classes[arg]()
            models.storage.new(model)
            models.storage.save()
            print(model.id)
        except Exception as e:
            print(e)

    def do_show(self, arg):
        """Display the string representation of a class instance of a given id"""
        if arg == "":
            print('** class name missing **')
            return

        try:
            model_name, model_id = arg.split(' ')
            model = models.storage.find(model_name, model_id)
            print(model.__str__())

        except Exception as e:

            if arg.count(' ') == 0:
                print("** instance id missing **")
            elif arg.count(' ') > 1:
                print("** too many arguments (2 arguments required)**")
            else:
                print(e)
    def do_destroy(self, arg):
        """Delete a class instance of a given id"""
        if arg == "":
            print('** class name missing **')
            return

        try:
            model_name, model_id = arg.split(' ')
            models.classes[model_name]  # check the model is supported
            models.storage.delete(model_name, model_id)
            models.storage.save()

        except Exception as e:

            if arg.count(' ') == 0:
                print("** instance id missing **")
            elif arg.count(' ') > 1:
                print("** too many arguments (2 arguments required)**")
            else:
                print(e)

    def do_all(self, arg):
        """Display string representations of all instances of a given class"""
        if arg == "":
            print([x.__str__() for x in models.storage.all().values()])
        else:
            try:
                model = models.classes[arg]
                resp = []
                for l in models.storage.all().values():
                    if type(l) == model:
                        resp.append(l.__str__())
                print(resp)
            except Exception as e:
                print(e)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        if arg == "":
            print('** class name missing **')
            return

        try:
            # TODO: Handle case where the value to update has a space character
            model_name, model_id, attr, value = arg.split(' ')

            models.storage.update(model_name, model_id, attr, value)
            models.storage.save()

        except Exception as e:
            if arg.count(' ') == 0:
                print("** instance id missing **")
            elif arg.count(' ') == 1:
                print("** attribute name missing **")
            elif arg.count(' ') == 2:
                print("** value missing **")
            elif arg.count(' ') > 3:
                # TODO: Allow this case, and ignore the extra arguments
                print("** too many arguments (2 arguments required)**")
            else:
                print(e)



if __name__ == '__main__':
    HBNBCommand().cmdloop()