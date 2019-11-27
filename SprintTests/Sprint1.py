# -*- coding: utf-8 -*-

import unittest
import GedRead
from GedMembers import Valid
from GedMembers import individual
from GedMembers import family
from GedHelper import gedHelper
from GedUtil import gedUtil


# from pytest import ExitCode

class test_ged(unittest.TestCase):

    def test_marriageBeforeDeath(self):
        indiRight = individual("No1", name="Li Four", marrigeDate="14 SEP 1990", death="14 SEP 1996")
        indiWrong = individual("No1", name="Li Four", marrigeDate="14 SEP 1997", death="14 SEP 1996")
        self.assertTrue(gedHelper().marriageBeforeDeath(indiRight))
        self.assertFalse(gedHelper().marriageBeforeDeath(indiWrong))
    
    def test_divorceBeforeDeath(self):
        indiRight = individual("No2", name="Li Four", divorceDate="14 SEP 1990", death="14 SEP 1996")
        indiWrong = individual("No2", name="Li Four", divorceDate="14 SEP 1997", death="14 SEP 1996")
        self.assertTrue(gedHelper().divorceBeforeDeath(indiRight))
        self.assertFalse(gedHelper().divorceBeforeDeath(indiWrong))


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False)
