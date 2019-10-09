# -*- coding: utf-8 -*-

import unittest
import GedRead
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
        self.assertNotIn(GedRead.readGed('SameIDDIfferentName.ged'), 'Name is: Robert /Smith/')    

    def test_sameName_individual(self):
        GedRead.indList = []
        GedRead.famList = []
        GedRead.linedataList = [] 
        self.assertNotIn(GedRead.readGed('SameNameDifferentId.ged'), 'ID is: @I2@')

    def test_over_fivethousand_ind(self):
        GedRead.indList = []
        GedRead.famList = []
        GedRead.linedataList = []
        self.assertNotIn(GedRead.readGed('Over 5000 Ind 1000 Fam.ged'), 'Name is: 5001 /5001/')

    def test_over_thousand_fam(self):
        GedRead.indList = []
        GedRead.famList = []
        GedRead.linedataList = [] 
        self.assertNotIn(GedRead.readGed('Over 5000 Ind 1000 Fam.ged'), 'Family ID is: @F1001')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False)
