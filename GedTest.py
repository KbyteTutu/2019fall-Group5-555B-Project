# -*- coding: utf-8 -*-

import unittest
import GedRead
from GedMembers import Valid
from GedMembers import individual
from GedMembers import family
#from pytest import ExitCode


class test_ged(unittest.TestCase):

    def test_read_ged_validity(self):
        self.assertEqual(GedRead.readGed('24234231234.ged'), 'invalid')
        self.assertEqual(GedRead.readGed('WrongSex.ged'), 'invalid')
        self.assertEqual(GedRead.readGed('FliipedHusbWife.ged'), 'invalid')
        self.assertEqual(GedRead.readGed('Group 5 GED.ged'), 'valid')


    def test_sameID_or_sameName_individual(self):
        temp = []
        GedRead.readGedTest('SameIDDIfferentName.ged', temp, True)
        self.assertNotIn('Robert /Smith/', temp)
        temp = []
        GedRead.readGedTest('SameNameDifferentId.ged', temp, True)
        self.assertNotIn('@I2@', temp)

    # def test_invalid_amount_ind_and_fam(self):
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
        temp = []
        GedRead.readGed('SameIDFamily.ged')
        for j in GedRead.famList:
            if j.wifeN is not None:
                temp.append(j.wifeN)
        print(*temp, sep='\n')
        self.assertNotIn('Tina /Bush/', temp)

    def test_create_class(self):
        print("~~~Test Create~~~~")
        testIndi = individual(indi="test", name="test")
        testIndi.printInfo()
        self.assertEqual(testIndi.indi, "test")
        testFamily = family(famid="testFam", wife="Godzilla")
        testFamily.printBriefInfo()
        self.assertEqual(testFamily.wife, "Godzilla")
        print("~~~Test Create~~~~")


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False)
