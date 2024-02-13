#!/usr/bin/python3

import cmd
import models
from shlex import split as split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

new_classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
        'Amenity': Amenity, 'Place': Place, 'City': City,
        'Review': Review}

class HBNBCommand(cmd.Cmd):
    """
    command interpreter
    """

    prompt = "(hbnb) "

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        class_name = line.split()
        if not class_name:
            print("** class name missing **")
        elif class_name[0] not in new_classes.keys():
            print("** class doesn't exist **")
        else:
            new_instance = new_classes[class_name[0]]()
            print(new_instance.id)
            new_instance.save()

    def do_show(self, line):
        """Prints the string representation of an instance
         based on the class name and id
         """
        store = {}
        content = line.split()
        if len(content) < 1:
            print("** class name missing **")
        elif content[0] not in new_classes.keys():
            print("** class doesn't exist **")
        elif len(content) < 2:
            print("** instance id missing **")
        else:
            class_name, instance_id = content[0], content[1]
            instance_key = f"{class_name}.{instance_id}"
            store = models.storage.all()
            if instance_key in store.keys():
                print(store[instance_key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on `class name` and `id`"""
        store = {}
        content = line.split()
        if len(content) < 1:
            print("** class name missing **")
        elif content[0] not in new_classes.keys():
            print("** class doesn't exist **")
        elif len(content) < 2:
            print("** instance id missing **")
        else:
            class_name, instance_id = content[0], content[1]
            instance_key = f"{class_name}.{instance_id}"
            store = models.storage.all()
            if instance_key in store.keys():
                del store[instance_key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """
        store = {}
        content = line.split()
        if len(content) < 1:
            print("** class name missing **")
        elif content[0] not in new_classes.keys():
            print("** class doesn't exist **")
        elif len(content) == 1:
            print("** instance id missing **")
        elif len(content) == 2:
            print("** attribute name missing **")
        elif len(content) == 3:
            print("** value missing **")

        else:
            class_name, instance_id = content[0], content[1]
            store = models.storage.all()
            if f"{class_name}.{instance_id}" in store.keys():
                setattr(store[f"{class_name}.{instance_id}"],
                        content[2], content[3])
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Method to print all instances based or not class name"""

        obj_list = []
        obj_dict = models.storage.all()

        if not line:
            for instance in obj_dict.values():
                obj_list.append(str(instance))
        else:
            content = line.split()
            if content[0] in new_classes:
                for key, value in obj_dict.items():
                    if value.__class__.__name__ == content[0]:
                        obj_list.append(str(value))
            else:
                print("** class doesn't exist **")
                return False
        print(obj_list)

    def default(self, line):
        """
        Parses a line and executes methods outside of those defined
        above
        """
        count = 0

        data = line.split('.', 1)
        if len(data) >= 2:
            line = data[1].split('(')
            """executes `.all()` method on a class instance"""
            if line[0] == "all":
                self.do_all(data[0])
                """executes `.count()` method"""
            elif line[0] == "count":
                for key in models.storage.all().keys():
                    if key.split('.')[0] == data[0]:
                        count += 1
                print(count)
                """executes `.show()` method on a class instance"""
            elif line[0] == "show":
                class_id = line[1].rstrip(')')
                param = f"{data[0]} {class_id}"
                self.do_show(param)
            elif line[0] == "destroy":
                class_id = line[1].rstrip(')')
                param = f"{data[0]} {class_id}"
                self.do_destroy(param)
            elif line[0] == "update":
                update = line[1].split(')')
                string = update[0].split('{')
                if len(string) == 1:
                    content = update[0].split(',')
                    self.do_update(f"{data[0]} {content[0]} {content[1]} {content[2]}")
                else:
                    class_id = string[0][:-2]
                    str_dict = string[1][:-1]
                    delim = str_dict.split(',')
                    for row in delim:
                        key_value = row.split(':')
                        param = f"{data[0]} {class_id} {key_value[0]} {key_value[1]}"
                        self.do_update(param)

    def emptyline(self):
        """ Shouldn’t execute anything. """
        pass

    def do_quit(self, line):
        """Quit command to exit the program USAGE: <quit>"""
        return True

    def do_EOF(self, line):
        """quits the console USAGE: <ctrl + 'D'>"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

