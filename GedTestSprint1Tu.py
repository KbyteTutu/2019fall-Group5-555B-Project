# -*- coding: utf-8 -*-

import unittest
import GedRead
from GedMembers import Valid
from GedMembers import individual
from GedMembers import family
from GedHelper import gedHelper
from GedUtil import gedUtil
#from pytest import ExitCode

class test_ged(unittest.TestCase):

    #Rh
    def test_datebeforeCurrentdate(self):
        indiRight = individual("No1", name="Zhang Three", birth="14 SEP 1996", death="15 SEP 1996", marrigeDate="10 OCT 2011",divorceDate="11 OCT 2012")
        indiWrong = individual("No1", name="Zhang Three", birth="14 SEP 2020", death="15 SEP 2020", marrigeDate="10 OCT 2020",divorceDate="11 OCT 2020")
        self.assertTrue(gedHelper().datebeforeCurrentdate(indiRight))
        self.assertFalse(gedHelper().datebeforeCurrentdate(indiWrong))

    def test_birthBeforeMarriage(self):
        indiRight = individual("No2", name="Li Four", birth="14 SEP 1990", marrigeDate="14 SEP 1996")
        indiWrong = individual("No2", name="Li Four", birth="14 SEP 1997", marrigeDate="14 SEP 1996")
        self.assertTrue(gedHelper().birthBeforeMarriage(indiRight))
        self.assertFalse(gedHelper().birthBeforeMarriage(indiWrong))
    #/Rh

    #Kt Sprint1
    def test_birthBeforeDeath(self):
        indiRight = individual("No1",name="Zhang Three",birth="14 SEP 1996",death="15 SEP 1996")
        indiWrong = individual("No1",name="Zhang Three",birth="14 SEP 1996",death="15 SEP 1995")
        self.assertTrue(gedHelper().birthBeforeDeath(indiRight))
        self.assertFalse(gedHelper().birthBeforeDeath(indiWrong))

    def test_marriageBeforeDivorce(self):
        indiRight = individual("No2",name="Li Four",marrigeDate="14 SEP 1996",divorceDate="15 SEP 1996")
        indiWrong = individual("No2",name="Li Four",marrigeDate="14 SEP 1996",divorceDate="13 SEP 1996")
        self.assertTrue(gedHelper().marriageBeforeDivorce(indiRight))
        self.assertFalse(gedHelper().marriageBeforeDivorce(indiWrong))

    #/Kt Sprint1


    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False)
