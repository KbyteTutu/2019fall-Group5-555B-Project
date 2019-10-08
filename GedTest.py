# -*- coding: utf-8 -*-

import unittest
import GedRead

class ged_test(unittest.TestCase):
    def test_validity(self):
        self.assertEquals(readGed('Sweden2.jpg'), 'invalid')
        self.assertEquals(readGed('Group 5 GED.ged'), 'valid')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
