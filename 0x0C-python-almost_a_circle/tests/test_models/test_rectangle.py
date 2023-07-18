#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.base import Base
import io
from contextlib import redirect_stdout


class TestRectangle(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0
        self.valid_rec_1 = Rectangle(5, 4, 2, 1)
        self.valid_rec_2 = Rectangle(5, 4, 2, 1, 34)
        self.valid_rec_3 = Rectangle(5, 4, 2, 1)
        self.valid_rec_4 = Rectangle(5, 4, 2, 1)
        self.valid_rec_6 = Rectangle(5, 4, 2, 1)
        self.valid_rec_7 = Rectangle(5, 4, 2, 1, 34)
        self.large_rec = Rectangle(5**6, 4**6)

    def tearDown(self):
        pass

    """test the instantiation"""
    def test_instant(self):
        tp = "<class 'models.rectangle.Rectangle'>"
        self.assertEqual(str(type(self.valid_rec_1)), tp)
        self.assertTrue(isinstance(self.valid_rec_1, Rectangle))
        self.assertTrue(issubclass(Rectangle, Base))

    def test_constraction(self):
        with self.assertRaises(TypeError):
            rc = Rectangle()
        with self.assertRaises(TypeError):
            rc = Rectangle(1, 2, 3, 4, 5, 6, 7)
        with self.assertRaises(TypeError):
            rc = Rectangle(2)
        self.assertEqual(Rectangle(1, 2).__str__(),
                         '[Rectangle] (6) 0/0 - 1/2')
        self.assertEqual(Rectangle(1, 2, 3).__str__(),
                         '[Rectangle] (7) 3/0 - 1/2')

    def test_attr(self):
        """test the object representation"""
        dictt = {'_Rectangle__width': 5, '_Rectangle__height': 4,
                 '_Rectangle__x': 2, '_Rectangle__y': 1, 'id': 34}
        self.assertDictEqual(self.valid_rec_2.__dict__, dictt)

    """Testing the exceptions for each attribute"""
    def test_width(self):
        """Testing attribute width"""
        with self.assertRaises(ValueError):
            Rectangle(-2, 5)
        with self.assertRaises(ValueError):
            Rectangle(0, 5)
        with self.assertRaises(TypeError):
            Rectangle("g", 5)
        with self.assertRaises(TypeError):
            Rectangle(3.6, 5)

    def test_height(self):
        """Testing attribute height"""
        with self.assertRaises(ValueError):
            Rectangle(2, -5)
        with self.assertRaises(ValueError):
            Rectangle(3, 0)
        with self.assertRaises(TypeError):
            Rectangle(6, "5")
        with self.assertRaises(TypeError):
            Rectangle(3, 5.6)

    def test_x(self):
        """Testing attribute x"""
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -1)
        with self.assertRaises(TypeError):
            Rectangle(5, 10, 2.5)

    def test_y(self):
        """Testing attribute y"""
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 0, -1)
        with self.assertRaises(TypeError):
            Rectangle(5, 10, 0, 2.5)

    """Testing a valid instance of Rectangle"""
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

        self.assertEqual(self.valid_rec_2.x, 2)

        self.valid_rec_2.x = 4

        self.assertEqual(self.valid_rec_2.x, 4)
        self.assertEqual(self.valid_rec_1.x, 2)

        self.valid_rec_1.x = 4

        self.assertEqual(self.valid_rec_1.x, 4)

        self.assertEqual(self.valid_rec_2.height, 4)

        self.valid_rec_2.height = 45

        self.assertEqual(self.valid_rec_2.height, 45)
        self.assertEqual(self.valid_rec_1.height, 4)

        self.valid_rec_1.height = 46

        self.assertEqual(self.valid_rec_1.height, 46)

        self.assertEqual(self.valid_rec_2.y, 1)

        self.valid_rec_2.y = 487

        self.assertEqual(self.valid_rec_2.y, 487)
        self.assertEqual(self.valid_rec_1.y, 1)

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
        self.assertEqual(self.large_rec.area(), 64000000)
        self.assertEqual(self.valid_rec_1.area(), 20)
        with self.assertRaises(TypeError):
            Rectangle.area()

    def test_display(self):
        """testing the display"""
        std = io.StringIO()
        with redirect_stdout(std):
            self.valid_rec_1.display()
            out = "\n  #####\n  #####\n  #####\n  #####\n"
            self.assertEqual(std.getvalue(), out)
        std = io.StringIO()
        r3 = Rectangle(1, 1, 12, 12, 5)
        with redirect_stdout(std):
            r3.display()
            res = "\n\n\n\n\n\n\n\n\n\n\n\n            #\n"
            self.assertEqual(std.getvalue(), res)
        with self.assertRaises(TypeError):
            Rectangle.display()
        r4 = Rectangle(1, 2)
        std = io.StringIO()
        with redirect_stdout(std):
            res = "#\n#\n"
            r4.display()
            self.assertEqual(std.getvalue(), res)
        r5 = Rectangle(1, 2, 3)
        std = io.StringIO()
        with redirect_stdout(std):
            res = "   #\n   #\n"
            r5.display()
            self.assertEqual(std.getvalue(), res)

    def test_str(self):
        """this for testing the print"""
        self.assertEqual(self.valid_rec_7.__str__(),
                         "[Rectangle] (34) 2/1 - 5/4")
        self.assertNotEqual(self.valid_rec_6.__str__(),
                            "[Rectangle] (6) 2/1 - 5/4")

    def test_update(self):
        """this for testing the update function"""
        output = "[Rectangle] (89) 4/5 - 2/3"
        self.valid_rec_7.update(89, 2, 3, 4, 5)
        self.assertEqual(self.valid_rec_7.__str__(), output)

        output = "[Rectangle] (8) 4/5 - 2/3"
        self.valid_rec_7.update(8)
        self.assertEqual(self.valid_rec_7.__str__(), output)

        with self.assertRaises(TypeError):
            self.valid_rec_7.update(89, "j", 3, 4, 5)
        with self.assertRaises(TypeError):
            self.valid_rec_7.update(89, 3, "k", 4, 5)
        with self.assertRaises(TypeError):
            self.valid_rec_7.update(89, 3, 3, "o", 5)
        with self.assertRaises(TypeError):
            self.valid_rec_7.update(89, 6, 3, 4, "p")

        with self.assertRaises(ValueError):
            self.valid_rec_7.update(89, 0, 3, 4, 5)
        with self.assertRaises(ValueError):
            self.valid_rec_7.update(89, 3, 0, 4, 5)
        with self.assertRaises(ValueError):
            self.valid_rec_7.update(89, 3, 3, -1, 5)
        with self.assertRaises(ValueError):
            self.valid_rec_7.update(89, 6, 3, 4, -1)

    def test_to_dictionary(self):
        """test the dectionary function"""
        r1 = Rectangle(5, 4, 2, 1, 34)
        res = {'id': 34, 'height': 4, 'width': 5, 'x': 2, 'y': 1}
        self.assertEqual(r1.to_dictionary(), res)

        r2 = Rectangle(5**6, 5**6, 5**6, 5**6, 41)
        res_2 = {'id': 41, 'height': 15625, 'width': 15625,
                 'x': 15625, 'y': 15625}
        self.assertEqual(r2.to_dictionary(), res_2)

    def test_inheitence(self):
        """test inharitence of the reactangle"""
        Base._Base__nb_objects = 2
        rec = Rectangle(12, 4, 2, 3)
        self.assertEqual(rec.id, 3)


if __name__ == "__main__":
    unittest.main()
