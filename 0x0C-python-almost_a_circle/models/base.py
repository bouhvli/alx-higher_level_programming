#!/usr/bin/python3
"""this model will create the base model"""
import json
import csv


class Base:
    """this the base class representation"""
    __nb_objects = 0

    def __init__(self, id=None):
        """the Base constructor method"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """this methode will convert the list of dict
        into a string"""
        if (list_dictionaries is None) or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """this function will convert the string to json"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """this function will save_to_file """
        if (list_objs is None):
            list_objs = []

        file_name = cls.__name__ + ".json"
        tr = [obj.to_dictionary() for obj in list_objs]
        my_dict = cls.to_json_string(tr)
        with open(file_name, "w") as file:
            file.write(my_dict)

    @classmethod
    def create(cls, **dictionary):
        """this will create an object from the class"""
        class_name = cls.__name__
        if (class_name == "Rectangle"):
            my_dict = cls(1, 1)
            my_dict.update(**dictionary)
            return (my_dict)
        if (class_name == "Square"):
            my_dict = cls(1)
            my_dict.update(**dictionary)
            return (my_dict)

    @classmethod
    def load_from_file(cls):
        """this function will load the objects from file"""
        from os import path
        list_obj = []
        file_name = cls.__name__ + ".json"
        if not path.isfile(file_name):
            return []
        with open(file_name, "r") as file:
            line = file.readline()
            string = cls.from_json_string(line)
            for item in string:
                list_obj.append(cls.create(**item))
            return list_obj

    @classmethod
    def save_to_file_csv(cls, list_objs):
        from models.rectangle import Rectangle
        from models.square import Square
        if (list_objs is None):
            list_objs = []

        file_name = cls.__name__ + ".csv"
        if cls is Square:
            list_objs = [[el.id, el.size, el.x, el.y]
                         for el in list_objs]
        elif cls is Rectangle:
            list_objs = [[el.id, el.width, el.height, el.x, el.y]
                         for el in list_objs]
        with open(file_name, "w", encoding="UTF-8") as file:
            printer = csv.writer(file)
            printer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """this function will load the objects from file"""
        from models.rectangle import Rectangle
        from models.square import Square
        list_obj = []
        file_name = cls.__name__ + ".csv"
        with open(file_name, "r", newline='', encoding="UTF-8") as file:
            test = csv.reader(file)
            for row in test:
                if len(row) < 4:
                    return []
                row = [int(item) for item in row]
                if (cls is Square):
                    res = {
                        "id": row[0], "size": row[1],
                        "x": row[2], "y": row[3]
                        }
                else:
                    res = {
                        "id": row[0], "width": row[1],
                        "height": row[2], "x": row[3],
                        "y": row[4]
                        }
                list_obj.append(cls.create(**res))
            return list_obj
