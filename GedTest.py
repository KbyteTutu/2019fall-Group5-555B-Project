# -*- coding: utf-8 -*-

import unittest
import GedRead
from GedMembers import Valid
from GedMembers import individual
from GedMembers import family
#from pytest import ExitCode


class test_ged(unittest.TestCase):

    def test_ged_validity(self):
        self.assertEqual(GedRead.readGed('24234231234.ged'), 'invalid')
        self.assertEqual(GedRead.readGed('Group 5 GED.ged'), 'valid')


    def test_same_ID_or_Name_individual(self):
        GedRead.indList = []
        GedRead.famList = []
        GedRead.linedataList = []
        temp = []
        GedRead.readGedTest('SameIDDIfferentName.ged', temp, True)
        self.assertEqual(GedRead.readGed('SameIDDifferentName.ged'), 'valid')
        self.assertNotIn('Robert /Smith/', temp)
        GedRead.indList = []
        GedRead.famList = []
        GedRead.linedataList = []
        temp = []
        GedRead.readGedTest('SameNameDifferentId.ged', temp, True)
        self.assertEqual(GedRead.readGed('SameNameDifferentId.ged'), 'valid')
        self.assertNotIn('@I2@', temp)

    # def test_amount_ind_and_fam(self):
    #    GedRead.indList = []
    #    GedRead.famList = []
    #    GedRead.linedataList = []
    #    temp = []
    #    GedRead.readGed('Over 5000 Ind 1000 Fam.ged')
    #    for j in GedRead.indList:
    #        if j.name is not None:
    #            temp.append(j.name)
    #    self.assertNotIn('Name is: 5001 /5001/', temp)
    #    GedRead.indList = []
    #    GedRead.famList = []
    #    GedRead.linedataList = []
    #    temp = []
    #    GedRead.readGed('Over 5000 Ind 1000 Fam.ged')
    #    for j in GedRead.indList:
    #        if j.indi is not None:
    #            temp.append(j.indi)
    #    self.assertNotIn('@F1001@', temp)
    #                                                       WARNING THE ABOVE TESTS WILL RUN FOR A WHILE UNCOMMENT THEM IF PREPARED TO WAIT


    def test_sameID_family(self):
        GedRead.indList = []
        GedRead.famList = []
        GedRead.linedataList = []
        temp = []
        GedRead.readGed('SameIDFamily.ged')
        self.assertEqual(GedRead.readGed('SameIDFamily.ged'), 'valid')
        for j in GedRead.famList:
            if j.wifeN is not None:
                temp.append(j.wifeN)
        print(*temp, sep='\n')
        self.assertNotIn('Tina /Bush/', temp)

    def test_create_class(self):
        GedRead.indList = []
        GedRead.famList = []
        GedRead.linedataList = []
        print("~~~Test Create~~~~")
        testIndi = individual(indi="test", name="test")
        testIndi.printInfo()
        self.assertEqual(testIndi.indi, "test")
        testFamily = family(famid="testFam", wife="Godzilla")
        testFamily.printBriefInfo()
        self.assertEqual(testFamily.wife, "Godzilla")
        print("~~~Test Create~~~~")

    def test_check_Sex_and_HusbWife(self):
        GedRead.indList = []
        GedRead.famList = []
        GedRead.linedataList = []
        GedRead.readGed('WrongSex.ged')
        self.assertEqual(GedRead.readGed('WrongSex.ged'), 'valid')
        self.assertFalse(GedRead.validate_family(GedRead.indList, GedRead.famList))
        GedRead.indList = []
        GedRead.famList = []
        GedRead.linedataList = []
        GedRead.readGed('FlippedHusbWife.ged')
        self.assertEqual(GedRead.readGed('FlippedHusbWife.ged'), 'valid')
        self.assertFalse(GedRead.validate_family(GedRead.indList, GedRead.famList))

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False)
