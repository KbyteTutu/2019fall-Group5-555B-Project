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

    #Sb
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

    #Na
    def test_validBirth(self):
        individuals = []
        families = []
        indi_1 = individual("1", name = "Test", birth = "14 SEPT 1996", death = "14 SEPT 2019", marrigeDate="14 SEPT 2018", family="1")
        indi_2 = individual("2", name = "Test2", birth = "15 SEPT 1996", death = "15 SEPT 2019", marrigeDate="14 SEPT 2018", family="1")
        indi_3 = individual("3", name = "Test3", birth = "16 SEPT 2019")
        indi_3.familyC = "1"
        individuals.append(indi_1)
        individuals.append(indi_2)
        individuals.append(indi_3)
        fam_1 = family("1", husband= "1", wife= "2", children= ["3"], marDate= "14 SEPT 2018")
        families.append(fam_1)
        self.assertFalse(gedHelper().validBirth(individuals,families))
        individuals.pop()
        families.pop()
        indi_4 = individual("3", name = "Test3", birth = "16 SEPT 2018")
        indi_4.familyC = "1"
        individuals.append(indi_4)
        fam_2 = family("1", husband= "1", wife= "2", children= ["3"], marDate= "14 SEPT 2018")
        families.append(fam_2)
        self.assertTrue(gedHelper().validBirth(individuals,families))
        
    def test_validMarriage(self):
        individuals = []
        families = []
        indi_1 = individual("1", name = "Test", birth = "14 SEPT 1996", death = "14 SEPT 2019", marrigeDate="14 SEPT 2018", family="1")
        indi_2 = individual("2", name = "Test2", birth = "15 SEPT 2017", death = "15 SEPT 2019", marrigeDate="14 SEPT 2018", family="1")
        individuals.append(indi_1)
        individuals.append(indi_2)
        fam_1 = family("1", husband= "1", wife= "2", marDate= "14 SEPT 2018")
        families.append(fam_1)
        self.assertFalse(gedHelper().validMarriage(individuals,families))
        individuals.pop()
        families.pop()
        indi_4 = individual("2", name = "Test2", birth = "15 SEPT 1996", death = "15 SEPT 2019", marrigeDate="14 SEPT 2018", family="1")
        individuals.append(indi_4)
        fam_2 = family("1", husband= "1", wife= "2", marDate= "14 SEPT 2018")
        families.append(fam_2)
        self.assertTrue(gedHelper().validMarriage(individuals,families))

    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False)
