# -*- coding: utf-8 -*-

import unittest
import GedRead
from GedMembers import Valid
from GedMembers import individual
from GedMembers import family
#from pytest import ExitCode

class test_ged(unittest.TestCase):
    def test_read_ged_invalidity(self):
        GedRead.indList = []
        GedRead.famList = []
        GedRead.linedataList = [] 
        self.assertEqual(GedRead.readGed('24234231234.ged'), 'invalid')

    def test_read_ged_validity(self):
        GedRead.indList = []
        GedRead.famList = []
        GedRead.linedataList = [] 
        self.assertEqual(GedRead.readGed('Group 5 GED.ged'), 'valid')

    def test_sameID_individual(self):
        GedRead.indList = []
        GedRead.famList = []
        GedRead.linedataList = [] 
        temp = []
        GedRead.readGed('SameIDDIfferentName.ged')
        for j in GedRead.indList:
            if j.name is not None:
                temp.append(j.name)
        self.assertNotIn('Robert /Smith/', temp)    

    def test_sameName_individual(self):
        GedRead.indList = []
        GedRead.famList = []
        GedRead.linedataList = [] 
        temp = []
        GedRead.readGed('SameNameDifferentId.ged')
        for j in GedRead.indList:
            if j.indi is not None:
                temp.append(j.indi)
        self.assertNotIn('@I2@', temp)

    #def test_over_fivethousand_ind(self):
    #    GedRead.indList = []
    #    GedRead.famList = []
    #    GedRead.linedataList = []
    #    temp = []
    #    GedRead.readGed('Over 5000 Ind 1000 Fam.ged')
    #    for j in GedRead.indList:
    #        if j.name is not None:
    #            temp.append(j.name)
    #    self.assertNotIn('Name is: 5001 /5001/', temp)
    #                                                       WARNING THE ABOVE AND BELOW TESTS WILL RUN FOR A WHILE UNCOMMENT THEM IF PREPARED TO WAIT   
    #def test_over_thousand_fam(self):
    #    GedRead.indList = []
    #    GedRead.famList = []
    #    GedRead.linedataList = []
    #    temp = []
    #    GedRead.readGed('Over 5000 Ind 1000 Fam.ged')
    #    for j in GedRead.indList:
    #        if j.indi is not None:
    #            temp.append(j.indi)
    #    self.assertNotIn('@F1001@', temp)

    # def test_sameID_family(self):
    #     GedRead.indList = []
    #     GedRead.famList = []
    #     GedRead.linedataList = []
    #     temp = []
    #     GedRead.readGed('SameIDFamily.ged')
    #     for j in GedRead.famList:
    #         if j.wifeN is not None:
    #             temp.append(j.wifeN)
    #     print(*temp, sep = '\n')
    #     self.assertNotIn('Tina /Bush/', temp)

 #Testing create new class and see if the input data is right and the missing data is showing in defualt value
    def test_create_class(self):
        print("~~~Test Create~~~~")
        testIndi = individual(indi="test",name="test")
        testIndi.printInfo()
        self.assertEqual(testIndi.indi,"test")
        testFamily = family(famid="testFam",wife="Godzilla")
        testFamily.printBriefInfo()
        self.assertEqual(testFamily.wife,"Godzilla")
        print("~~~Test Create~~~~")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False)
