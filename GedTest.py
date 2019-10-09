# -*- coding: utf-8 -*-

import unittest
import GedRead
from pytest import ExitCode

class test_ged(unittest.TestCase):
    def test_read_ged_validity(self):
        self.assertEqual(GedRead.readGed('24234231234.ged'), 'invalid')
        self.assertEqual(GedRead.readGed('Group 5 GED.ged'), 'valid')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False)
