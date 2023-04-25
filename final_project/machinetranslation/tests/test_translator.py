
""" module docstring """

""" import sys
sys.path.append('..') """

from machinetranslation import translator

import unittest

class testEnglishToFrench(unittest.TestCase):
    """ class docstring """
    def test1(self):
        """ function docstring """
        # test for null input
        with self.assertRaises(TypeError) as cm:
            translator.englishToFrench(None)
            print('123')
        self.assertEqual(str(cm.exception), "It is a type error, I confirm.")
        self.assertEqual(translator.englishToFrench('Hello'), 'Bonjour') # test

class testFrenchToEnglish(unittest.TestCase):
    """ class docstring """
    def test1(self):
        """ function docstring """
        # test for null input
        with self.assertRaises(TypeError) as cm:
            translator.frenchToEnglish(None)
            print('4')
        self.assertEqual(str(cm.exception), "It is a type error, I confirm.")
        self.assertEqual(translator.frenchToEnglish('Bonjour'), 'Hello') # test

unittest.main()
