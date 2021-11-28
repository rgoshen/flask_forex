import unittest
from conversion import converter, get_symbol
from unittest import TestCase


class ConversionTestCase(TestCase):
    '''Tests conversion.'''

    def test_converter(self):
        '''Pass in same currency code for to and from and receive 1 back.'''
        self.assertEqual(converter('USD', 'USD', 1), 1.0)

    def test_get_symbol(self):
        '''Pass in currency code and receive back currency symbol.'''
        self.assertEqual(get_symbol('USD'), 'US$')


if __name__ == '__main__':
    unittest.main()
