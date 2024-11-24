
from unittest import TestCase, main
from random import random
from math import floor
from fundamentals import check_number

class MyTestCases(TestCase):
    def test_check_number_odd_number(self):
        for i in range(1, (floor(random() * 200) + 50), 2):
            self.assertEqual(check_number(i), 'Weird')

    def test_check_even_range_2_to_5(self):
        for i in range(2, 6, 2):
            self.assertEqual(check_number(i), 'Not Weird')

    def test_check_even_range_6_to_20(self):
        for i in range(6, 21, 2):
            self.assertEqual(check_number(i), 'Weird')

    def test_check_number_even_greater_than_20(self):
        for i in range(22, (floor(random() * 200) + 50), 2):
            self.assertEqual(check_number(i), 'Not Weird')

    def test_check_number_negative_even_number(self):
        for i in range(-2, -(floor(random() * 200) + 50), -2):
            self.assertEqual(check_number(i), 'Very Weird')

    def test_check_number_negative_odd_number(self):
        for i in range(-1, -(floor(random() * 200) + 50), -2):
            self.assertEqual(check_number(i), 'Extremely Weird')

    def test_check_number_neutral(self):
        self.assertEqual(check_number(0), 'Neutral')

    def test_check_number_even_number(self):
        for i in range(2, 6, 2):
            self.assertEqual(check_number(i), 'Not Weird')

        for i in range(6, 21, 2):
            self.assertEqual(check_number(i), 'Weird')

        for i in range(6, 21, 2):
            self.assertEqual(check_number(i), 'Weird')

if __name__ == '__main__': main()


