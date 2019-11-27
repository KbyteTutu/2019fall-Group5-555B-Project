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
    
    #US07
    def test_less_than_150_years(self):
        indi1 = individual("No1", name="Old", birth="1 JAN 1800")
        output = gedHelper().lessThan150Years(indi1)
        self.assertTrue(output == False)

    #US08
    def test_birth_before_marriage(self):
        indi1 = individual("No1", name="Mother", husbID="No2", marrigeDate="1 OCT 1990", family="1", familyC="1")
        indi2 = individual("No2", name="Father", wifeID="No1", marrigeDate="1 OCT 1990", family="1", familyC="1")
        indi3 = individual("No3", name="Child", birth="2 OCT 1990", family="1", familyC="1")
        fam1 = family("1", husband="No2", wife="No1")
        indList1 = [indi1, indi2, indi3]
        famList1 = [fam1]
        output = gedHelper().validMarriage(indList1, famList1)
        self.assertTrue(output == True)

    #US17
    def test_no_marriage_to_descendants(self):
        indi1 = individual("No1", name="Mother", husbID="No2", marrigeDate="1 OCT 1990", family="1", familyC="1")
        indi2 = individual("No2", name="Father", wifeID="No1", marrigeDate="1 OCT 1990", family="1", familyC="1")
        indi3 = individual("No3", name="Child", birth="2 OCT 1990", family="1", familyC="1", husbID="No2")
        fam1 = family("1", husband="No2", wife="No1")
        indList1 = [indi1, indi2, indi3]
        famList1 = [fam1]
        output = gedHelper().marriageToDescendant(indList1, famList1)
        self.assertTrue(output == False)

    #US18
    def test_sibling_marriage(self):
        indi1 = individual("No1", name="Mother", husbID="No2", family="1",)
        indi2 = individual("No2", name="Father", wifeID="No1", family="1")
        indi3 = individual("No3", name="Brother", family="1", wifeID="No4")
        indi4 = individual("No4", name="Sister", family="1", husbID="No3")
        fam1 = family("1", wife="No1", husband="No2", children=[indi3.indi, indi4.indi])
        indList1 = [indi1, indi2, indi3, indi4]
        famList1 = [fam1]
        output = gedHelper().siblingsMarried(indList1, famList1)
        self.assertTrue(output == False)

    #US27
    def test_include_ind_age(self):
        indi1 = individual("No1", birth="2 NOV 1995")
        output = gedUtil().getAge(indi1)
        self.assertTrue(output == 24)

    #US28
    def test_order_siblings_by_age(self):
        indi1 = individual("No1", name="Child1", family="1", birth="1 JAN 1995")
        indi2 = individual("No2", name="Child2", family="1", birth="1 JAN 1996")
        indi3 = individual("No3", name="Child3", family="1", birth="1 JAN 1994")
        fam1 = family("1", children=[indi1.indi, indi2.indi, indi3.indi])
        indList1 = [indi1, indi2, indi3]
        output = gedHelper().orderSibling(indList1, fam1)
        self.assertTrue(output[0] == indi3)
        self.assertTrue(output[1] == indi1)
        self.assertTrue(output[2] == indi2)

    #US37
    def test_list_recent_survivors(self):
        indi1 = individual("No1", death="23 NOV 2019")
        output = gedUtil().dateLessThanThirtyDays(indi1.death)
        self.assertTrue(output == True)

    #US38
    def test_list_upcoming_birthdays(self):
        indi1 = individual("No1", birth="1 DEC 1999", name="1")
        indi2 = individual("No2", birth="4 APR 1998", name="2")
        indList1 = [indi1, indi2]
        output = gedHelper().upcomingBirthdays(indList1)
        self.assertTrue(indi2 not in output)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False)
