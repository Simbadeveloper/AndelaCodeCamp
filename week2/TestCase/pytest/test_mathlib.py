import mathlib
import unittest
from mathlib import *

class Hessabu(unittest.TestCase):

 def test_calc_total(self):
    result = mathlib.calc_total(4,5)
    assert result == 9

 def test_calc_multiply(self):
    result = mathlib.calc_multiply(10,3)
    assert result == 30

 def test_calc_subtract(self):
    result =mathlib.calc_subtract(10,5)
    assert result == 5

 def test_calc_reminder(self):
    result = mathlib.calc_reminder(7,3)
    assert result == 1

 def test_calc_division(self):
    result = mathlib.calc_division(8,2)
    assert result == 4

if __name__ == '__main__':
    unittest.main()