#!/usr/bin/python3
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """test class for the Base"""
    def setUp(self):
        """setup the stage for the methods"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """teardown that doesn't teardown anything"""
        pass

    def test_id(self):
        """this methode will test the id """
        check = hasattr(Base, "_Base__nb_objects")
        self.assertEqual(check, True)

    def test_id_value(self):
        """this method will test the id initial value"""
        check = getattr(Base, "_Base__nb_objects")
        self.assertEqual(check, 0)

    def test_id_value_after(self):
        """this methode will check if the value of
        id is working as expected"""
        b1 = Base()
        check = Base._Base__nb_objects
        self.assertEqual(b1.id, check)
        b2 = Base()
        self.assertEqual(b2.id, check + 1)

    def test_construct(self):
        """this method check if the constructure is working fine"""
        b = Base()
        b_type = str(type(b))
        b_str_type = "<class 'models.base.Base'>"
        self.assertEqual(b_type, b_str_type)

    def test_constructor_none(self):
        """this method check if the constructor will raise an error"""
        with self.assertRaises(TypeError):
            Base.__init__()

    def test_constructor_with_args(self):
        """check the constructor with diff values"""
        b1 = Base(2)
        self.assertEqual(b1.id, 2)
        with self.assertRaises(TypeError):
            b2 = Base(3, 4, 5)

    def test_id_with_str(self):
        """test_id_ with an str value"""
        b1 = Base("baby")
        self.assertNotEqual(b1.id, 1)

    def check_sync_id_with_class(self):
        """this function test if the ids is synced properly"""
        b1 = Base()
        b1 = Base(id=22)
        self.assertEqual(b1.id, 22)
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
        b1 = Base()
        check = Base._Base__nb_objects
        self.assertEqual(b1, check)

    def test_to_json_string_edge(self):
        """test is the function to_json_string is workin properly
        as expected for the edge cases"""
        with self.assertRaises(TypeError):
            Base.to_json_string()

        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_to_json_string(self):
        """test is the function to_json_string is workin properly"""
        r2 = Rectangle(5**4, 7**3, 2**2, 8**12)
        dictionary_2 = r2.to_dictionary()
        json_dictionary_2 = Base.to_json_string([dictionary_2])
        check = '[{"id": 1, "height": 343,\
        "width": 625,"x": 4, "y": 68719476736}]'
        self.assertEqual(json_dictionary_2, check)
        self.assertEqual(len(json_dictionary_2), len(check))
        check = [{"id": 23}, {"life": 33}, {"cust": 12, "rest": 34}]
        b1 = Base.to_json_string(check)
        check_str = '[{"id": 23}, {"life": 33}, {"cust": 12, "rest": 34}]'
        self.assertEqual(b1, check_str)

        sq2 = Square(3**2, 10**5, 23)
        dic_2 = sq2.to_dictionary()
        json_dic_2 = Base.to_json_string([dic_2])
        check = '[{"id": 2, "size": 9, "x": 100000, "y": 23}]'
        self.assertEqual(json_dic_2, check)
        self.assertEqual(len(json_dic_2), len(check))

        sq1 = Square(4, 6, 9)
        req1 = Rectangle(23, 45, 66, 2)
        new_dic = [req1.to_dictionary(), r2.to_dictionary(),
                   sq1.to_dictionary(), sq2.to_dictionary()]
        to_json = Base.to_json_string(new_dic)
        old_way_dict = str(new_dic)
        old_way_dict = old_way_dict.replace("'", '"')
        self.assertEqual(to_json, old_way_dict)

    def test_from_json_string_edge(self):
        """test the function from_json_string edge case"""
        with self.assertRaises(TypeError):
            Base.from_json_string()
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string(self):
        """test the function from json to string"""
        sq2 = Square(3**2, 10**5, 23)
        dic_2 = sq2.to_dictionary()
        json_dic_2 = Base.to_json_string([dic_2])
        check = [{"id": 1, "size": 9, "x": 100000, "y": 23}]
        string_dic_2 = Base.from_json_string(json_dic_2)
        self.assertEqual(string_dic_2, check)

        o_str = '[{"id": 23}, {"life": 33}, {"cust": 12, "rest": 34}]'
        res = Base.from_json_string(o_str)
        o_str = [{"id": 23}, {"life": 33}, {"cust": 12, "rest": 34}]
        self.assertEqual(res, o_str)
        with self.assertRaises(TypeError):
            b = Base.from_json_string([{"id": 2, "height": 343,
                                        "width": 625, "x": 4,
                                        "y": 68719476736}])

    def test_save_to_file(self):
        """test the function save_to_file"""
        sq1 = Square(1, 3, 4)
        sq2 = Square(4, 67, 3)
        sq3 = Square(34, 45)
        Square.save_to_file([sq1, sq2, sq3])

        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 117)

    def test_save_to_file_edge(self):
        """test the function save_to_file for some edge cases"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_create(self):
        """test the create function in some cases"""
        sq = Square(12, 12, 3)
        sq_dict = sq.to_dictionary()
        sq1 = Square.create(**sq_dict)
        self.assertFalse(sq is sq1)
        self.assertEqual(str(sq), str(sq1))
        self.assertFalse(sq == sq1)

    def test_load_from_file(self):
        """test the load from file in some cases"""
        dic = []
        dic.append(Square(12, 23, 3))
        dic.append(Square(34, 45, 6))
        Square.save_to_file(dic)
        res = Square.load_from_file()
        self.assertEqual(str(dic[0]), str(res[0]))
        self.assertEqual(str(dic[1]), str(res[1]))
        self.assertNotEqual(id(dic[0]), id(res[0]))
        self.assertNotEqual(id(dic[1]), id(res[1]))

        dic = []
        dic.append(Rectangle(12, 23, 3, 4))
        dic.append(Rectangle(34, 45, 6, 5))
        Rectangle.save_to_file(dic)
        res = Rectangle.load_from_file()
        self.assertEqual(str(dic[0]), str(res[0]))
        self.assertEqual(str(dic[1]), str(res[1]))
        self.assertNotEqual(id(dic[0]), id(res[0]))
        self.assertNotEqual(id(dic[1]), id(res[1]))


if __name__ == "__main__":
    unittest.main()
