#!/usr/bin/python3
"""this model is for testing the square class"""
import unittest
from models.square import Square
from models.base import Base
import io
from contextlib import redirect_stdout


class TestSquare(unittest.TestCase):
    """In this class we will test the most possible edge cases"""
    def setUp(self):
        """setup someobject for the test"""
        Base._Base__nb_objects = 0
        self.valid_rec_1 = Square(5, 4, 2)
        self.valid_rec_2 = Square(5, 4, 2, 1)
        self.valid_rec_3 = Square(5, 4, 2)
        self.valid_rec_4 = Square(5, 4, 2)
        self.valid_rec_6 = Square(5, 4, 2)
        self.valid_rec_7 = Square(5, 4, 2, 34)
        self.large_rec = Square(5**6, 4**6)

    def tearDown(self):
        """doesn't tear anything down yet"""
        pass

    """test the instantiation"""
    def test_instant(self):
        """checking if the object is really what we want it to
        be"""
        tp = "<class 'models.square.Square'>"
        self.assertEqual(str(type(self.valid_rec_1)), tp)
        self.assertTrue(isinstance(self.valid_rec_1, Square))
        self.assertTrue(issubclass(Square, Base))

    def test_dict(self):
        """Testing the way the object stored"""
        res = {'_Rectangle__width': 5, '_Rectangle__height': 5,
               '_Rectangle__x': 10, '_Rectangle__y': 15, 'id': 2}
        self.assertEqual(Square(5, 10, 15, 2).__dict__, res)

    def test_constraction(self):
        """testing some edge cases"""
        with self.assertRaises(TypeError):
            rc = Square()
        with self.assertRaises(TypeError):
            rc = Square(1, 2, 3, 4, 5, 6, 7)
        with self.assertRaises(TypeError):
            rc = Square()

    def test_attr(self):
        """Testing the representation of the object"""
        dictt = {'_Rectangle__width': 5, '_Rectangle__height': 5,
                 '_Rectangle__x': 4, '_Rectangle__y': 2, 'id': 1}
        self.assertDictEqual(self.valid_rec_2.__dict__, dictt)

    def test_attr_kw(self):
        """Testing the representation of the object"""
        dictt = {'_Rectangle__width': 12, '_Rectangle__height': 12,
                 '_Rectangle__x': 15, '_Rectangle__y': 5, 'id': 10}
        sq = Square(y=5, id=10, x=15, size=12).__dict__
        self.assertEqual(sq, dictt)

    def test_attr_arg(self):
        """Testing the representation of the object"""
        dictt = {'_Rectangle__width': 5, '_Rectangle__height': 5,
                 '_Rectangle__x': 15, '_Rectangle__y': 12, 'id': 10}
        self.assertEqual(Square(5, id=10, x=15, y=12).__dict__,
                         dictt)
    """Testing the exceptions for each attribute"""
    def test_width(self):
        """Testing attribute width"""
        with self.assertRaises(ValueError):
            Square(-2, 5)
        with self.assertRaises(ValueError):
            Square(0, 5)
        with self.assertRaises(TypeError):
            Square("g", 5)
        with self.assertRaises(TypeError):
            Square(3.6, 5)

    def test_height(self):
        """Testing attribute height"""
        with self.assertRaises(ValueError):
            Square(2, -5)
        with self.assertRaises(ValueError):
            Square(0, 3)
        with self.assertRaises(TypeError):
            Square(6, "5")
        with self.assertRaises(TypeError):
            Square(3, 5.6)

    def test_x(self):
        """Testing attribute x"""
        with self.assertRaises(ValueError):
            Square(5, 10, -1)
        with self.assertRaises(TypeError):
            Square(5, 10, 2.5)

    def test_y(self):
        """Testing attribute y"""
        with self.assertRaises(TypeError):
            Square(5, 10, 0.5, 2)
        with self.assertRaises(ValueError):
            Square(5, 10, -5, 2)

    """Testing a valid instance of Square"""
    def test_valid_rec_id(self):
        """checking the id"""
        self.assertGreaterEqual(self.valid_rec_1.id, 1)
        self.assertNotEqual(self.valid_rec_2.id, 2)

        self.valid_rec_1.id = 12
        self.valid_rec_2.id = 12

        self.assertEqual(self.valid_rec_1.id, 12)
        self.assertEqual(self.valid_rec_2.id, 12)

    def test_valid_rec_attr(self):
        """checking all attributes"""
        self.assertEqual(self.valid_rec_2.width, 5)

        self.valid_rec_2.width = 4

        self.assertEqual(self.valid_rec_2.width, 4)
        self.assertEqual(self.valid_rec_1.width, 5)

        self.valid_rec_1.width = 4

        self.assertEqual(self.valid_rec_1.width, 4)

        self.assertEqual(self.valid_rec_2.x, 4)

        self.valid_rec_2.x = 4

        self.assertEqual(self.valid_rec_2.x, 4)
        self.assertEqual(self.valid_rec_1.x, 4)

        self.valid_rec_1.x = 4

        self.assertEqual(self.valid_rec_1.x, 4)

        self.assertEqual(self.valid_rec_2.height, 5)

        self.valid_rec_2.height = 45

        self.assertEqual(self.valid_rec_2.height, 45)
        self.assertEqual(self.valid_rec_1.height, 5)

        self.valid_rec_1.height = 46

        self.assertEqual(self.valid_rec_1.height, 46)

        self.assertEqual(self.valid_rec_2.y, 2)

        self.valid_rec_2.y = 487

        self.assertEqual(self.valid_rec_2.y, 487)
        self.assertEqual(self.valid_rec_1.y, 2)

        self.valid_rec_1.y = 0

        self.assertEqual(self.valid_rec_1.y, 0)

    def test_interfere(self):
        """this test is craeted to ensure the that multiple in stances
        of the class don't interfere with each other"""
        self.assertNotEqual(self.valid_rec_1.id, self.valid_rec_3)
        self.assertNotEqual(self.valid_rec_2.id, self.valid_rec_4)
        self.assertNotEqual(self.valid_rec_3.id, self.valid_rec_6)
        self.assertNotEqual(self.valid_rec_4.id, self.valid_rec_7)

    """the following tests will test the methodes inside the Rec
    class"""

    def test_area(self):
        """testin the area"""
        self.assertEqual(self.large_rec.area(), 244140625)
        self.assertEqual(self.valid_rec_1.area(), 25)
        with self.assertRaises(TypeError):
            Square.area()

    def test_display(self):
        """testing the display"""
        std = io.StringIO()
        with redirect_stdout(std):
            self.valid_rec_1.display()
            out = "\n\n    #####\n    #####\n    #####\n    #####\n    #####\n"
            self.assertEqual(std.getvalue(), out)
        std = io.StringIO()
        r3 = Square(1, 1, 12, 12)
        with redirect_stdout(std):
            r3.display()
            res = "\n\n\n\n\n\n\n\n\n\n\n\n #\n"
            self.assertEqual(std.getvalue(), res)
        with self.assertRaises(TypeError):
            Square.display()

    def test_str(self):
        """this for testing the print"""
        self.assertEqual(self.valid_rec_7.__str__(), "[Square] (34) 4/2 - 5")
        self.assertNotEqual(self.valid_rec_6.__str__(), "[Square] (6) 2/1 - 5")

    def test_update(self):
        """this for testing the update function"""
        output = "[Square] (89) 3/4 - 2"
        self.valid_rec_7.update(89, 2, 3, 4, 5)
        self.assertEqual(self.valid_rec_7.__str__(), output)

        output = "[Square] (8) 3/4 - 2"
        self.valid_rec_7.update(8)
        self.assertEqual(self.valid_rec_7.__str__(), output)

        with self.assertRaises(TypeError):
            self.valid_rec_7.update(89, "j", 3, 4)
        with self.assertRaises(TypeError):
            self.valid_rec_7.update(89, 3, "k", 4)
        with self.assertRaises(TypeError):
            self.valid_rec_7.update(89, 3, 3, "o")
        with self.assertRaises(TypeError):
            self.valid_rec_7.update(89, 6, 3, [4])

        with self.assertRaises(ValueError):
            self.valid_rec_7.update(89, 0, 3, 4, 5)
        with self.assertRaises(ValueError):
            self.valid_rec_7.update(89, 3, 3, -1, 5)
        with self.assertRaises(ValueError):
            self.valid_rec_7.update(89, 6, -3, 4)

    def test_to_dictionary(self):
        """Testing the dictionary function"""
        r1 = Square(5, 2, 1, 34)
        res = {'id': 34, 'size': 5, 'x': 2, 'y': 1}
        self.assertEqual(r1.to_dictionary(), res)

        r2 = Square(5**6, 5**6, 5**6, 41)
        res_2 = {'id': 41, 'size': 15625, 'x': 15625, 'y': 15625}
        self.assertEqual(r2.to_dictionary(), res_2)

    def test_inheitence(self):
        """testing the inhiritence"""
        Base._Base__nb_objects = 2
        rec = Square(12, 4, 2, 3)
        self.assertEqual(rec.id, 3)


if __name__ == "__main__":
    unittest.main()
