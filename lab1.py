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
class MusicalNote:
    pitch : float
    duration: int

#* Design Recipe
#* 1) convert celsius temp to fahrenheit
def celsius_to_fahrenheit(temp:Celsius) -> int:
    return (temp * 1.8) + 32
#* 2)
def up_one_octave(note: MusicalNote) -> MusicalNote:
    new_note = MusicalNote(note.pitch * 2, note.duration)
    return new_note

#* 3)
#* 4)
class TestClass(unittest.TestCase):
    def test_example(self):
        self.assertEqual( 1, 1 )
        #* 1)
    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0) , 32, 2)
        self.assertAlmostEqual(celsius_to_fahrenheit(17), 62.6, 2)
        self.assertAlmostEqual(celsius_to_fahrenheit(9), 48.2, 2)
        #* 2)
    def test_up_one_octave(self):
        self.assertAlmostEqual(up_one_octave(note1 = MusicalNote(2.5,3)), MusicalNote(5.0, 3), 1e-3)
        self.assertAlmostEqual(up_one_octave(note2 = MusicalNote(3, 5)), MusicalNote(6,5), 1e-3)
        self.assertAlmostEqual(up_one_octave(note3 = MusicalNote(4.356, 2)), MusicalNote(8.712, 2), 1e-3)
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