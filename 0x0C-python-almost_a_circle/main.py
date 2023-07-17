#!/usr/bin/python3
""" 14-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dictionary = Base.to_json_string([dictionary])

    sq2 = Square(3**2, 10**5, 23)
    dic_2 = sq2.to_dictionary()
    json_dic_2 = Base.to_json_string([dic_2])

    r2 = Rectangle(5**4, 7**3, 2**2, 8**12)
    dictionary_2 = r2.to_dictionary()
    json_dictionary_2 = Base.to_json_string([dictionary_2])
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))
    print("--------------------------------------")
    print(dictionary_2)
    print(type(dictionary_2))
    print(json_dictionary_2)
    print(type(json_dictionary_2))
    print("--------------------------------------")
    print(dic_2)
    print(type(dic_2))
    print(json_dic_2)
    print(type(json_dic_2))
    Rectangle.save_to_file(None)
    with open("Rectangle.json", "r") as file:
        print(file.read())
    valid_rec_2 = Square(5, 4, 2, 1)
    print(valid_rec_2.__dict__)

    print(Square(5, id = 10, x = 15, y=12).__dict__)
    print(valid_rec_2)