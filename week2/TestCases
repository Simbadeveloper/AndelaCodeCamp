"""
five testCases

"""
#usr/bin/python

import unittest
#import uniitest to use to test


def summ(first, second):
    """ sum of two numbers"""
    return first + second

def minus(first, second):
    """The difference of two numbers"""
    return first - second

def multiply(first, second):
    """muilplication of two numbers"""
    return first * second

def modulo(first, second):
    """The reminder"""
    return first  % second

def division(first, second):
    """division of two numbers"""
    return  first / second

#TestCases
#Test the function
class Hesabu(unittest.TestCase):
    """class that wrap the functions"""
    def testsumm(self):
        """Test for sum of numbers"""
        self.assertEqual(summ(4, 5), 9)

    def testminus(self):
        """Test the difference of two numbers"""
        self.assertEqual(minus(9, 5), 4)

    def testmultiply(self):
        """Test the multplication of two numbers"""
        self.assertEqual(multiply(4, 5), 20)

    def testmodulo(self):
        """Test the reminder after division of two numbers"""
        self.assertEqual(modulo(5, 4), 1)

    def testdivision(self):
        """Test the division of two number"""
        self.assertEqual(division(20, 4), 5)


if __name__ == '__main__':
    unittest.main()
