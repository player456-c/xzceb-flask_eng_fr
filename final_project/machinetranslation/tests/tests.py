
""" module docstring """

import sys
sys.path.append('..')

from translator import frenchToEnglish, englishToFrench

import unittest

class TestEnglishToFrench(unittest.TestCase):
    """ class docstring """
    def test1(self):
        """ function docstring """
        #self.assertEqual(englishToFrench(''), TypeError) # test for null input
        with self.assertRaises(TypeError) as cm:
            englishToFrench(None)
            print('123')
        self.assertEqual(str(cm.exception), "It is a type error, I confirm.")
        self.assertEqual(englishToFrench('Hello'), 'Bonjour') # test

class TestFrenchToEnglish(unittest.TestCase):
    """ class docstring """
    def test1(self):
        """ function docstring """
        #self.assertEqual(frenchToEnglish(), ) # test for null input
        with self.assertRaises(TypeError) as cm:
            frenchToEnglish(None)
            print('4')
        self.assertEqual(str(cm.exception), "It is a type error, I confirm.")
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') # test

unittest.main()
