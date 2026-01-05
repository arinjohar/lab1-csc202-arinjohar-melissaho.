from typing import *
from dataclasses import dataclass
import unittest
import sys
sys.setrecursionlimit(10**6)
#* Team-Member Intro Lines
#Hello I am Melissa.
#Hello I am AJ
#* Data Definitions
#* 1)

Celsius : TypeAlias = float
Fahrenheit : TypeAlias = float

#* 2)

@dataclass(frozen=True)
class Cents:
    price : int

#* 3)

@dataclass(frozen=True)
class PriceRecord:
    name : str
    price: Cents
    

#* 4)

@dataclass(frozen=True)
class PriceRecord:
    pitch : float
    duration: int

#* Design Recipe
#* 1)
#* 2)
#* 3)
#* 4)
class TestClass(unittest.TestCase):
    def test_example(self):
        self.assertEqual( 1, 1 )
        #* 1)
        #* 2)
        #* 3)
        #* 4)
        # If this is True, means this .py file is the .py being executed
        # (rather than being imported by the .py that is being executed).
        if (__name__ == '__main__'):
            print( "Running all defined tests:" )

            # What this does: find every class X that inherits from
            # unittest.TestCase (there are two in this file) and runs
            # every test defined inside X--every method whose name
            # begins with "test".
            unittest.main()