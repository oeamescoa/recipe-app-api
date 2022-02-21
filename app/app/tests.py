from django.test import TestCase
from app.calc import add, subtract

# this script is called by the Django framework when tests is passed in
# as a parameters to the python manage.py cmd; framework will instantiate
# a new class and call each instance method beginning with 'test' syntax

class CalcTests(TestCase):

    def test_add_numbers(self):
        '''Test that two numbers are added together'''
        self.assertEqual(add(3,8), 11)

    def test_subtract_numbers(self):
        '''Test that values are subtracted and returned'''
        self.assertEqual(subtract(5,11), 6)

        