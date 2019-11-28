# -*- coding: utf-8 -*-

import unittest
import GedRead
from GedMembers import Valid
from GedMembers import individual
from GedMembers import family
from GedHelper import gedHelper
from GedUtil import gedUtil
#from pytest import ExitCode
import copy

class test_ged(unittest.TestCase):
    #Sprint4
    #Rh
    def test_livingsingle(self):
        indi1 = individual("No1", name="Zhang 1", wifeID="Zhang 1", birth="10 OCT 1999", marrigeDate="10 OCT 2010", death="")
        indi2 = individual("No2", name="Zhang 2", husbID="Zhang 2", birth="10 OCT 1998", marrigeDate="10 OCT 2010", death="")
        indi3 = individual("No3", name="Zhang 3", wifeID="Zhang 3", birth="10 OCT 1997", marrigeDate="10 OCT 2010", death="")
        indi4 = individual("No4", name="Zhang 4", husbID="Zhang 4", birth="10 OCT 1916", death="")
        indi5 = individual("No5", name="Zhang 5", birth="10 OCT 1970", death="")
        fam1 = family("No1",  husband="Zhang 2",  wife="Zhang 1", children="Zhang 3")
        indList = [indi1,indi2,indi3,indi4,indi5]
        famList = [fam1]
        # self.assertTrue(gedHelper().livingsingle(indList,famList))


    def test_multiplebirths(self):
        indi1 = individual("No1", name="Zhang 1", wifeID="Zhang 1", birth="10 OCT 1900")
        indi2 = individual("No2", name="Zhang 2", husbID="Zhang 2", birth="10 OCT 1900")
        indi3 = individual("No3", name="Zhang 3", birth="10 OCT 1990")
        indi4 = individual("No4", name="Zhang 4", birth="10 OCT 1990")
        fam1 = family("No1",  husband="Zhang 2",  wife="Zhang 1", children="Zhang 3")
        indList = [indi1,indi2,indi3,indi4]
        famList = [fam1]
        self.assertTrue(gedHelper().multiplebirths(indList, famList))

    #Kt
    def test_listOrphans(self):
        indi1 = individual("No1", name="Orphan", birth="10 OCT 1900",age="10")

        indList = [indi1]
        a = gedHelper().listOrphans(indList)

        print(a)

        self.assertTrue(len(a)>0)
    
    def test_listLargeAgeDifference(self):
        indi1 = individual("No1", name="Zhang 1", birth="10 OCT 2000",age="19")
        indi2 = individual("No2", name="Zhang 2", birth="10 OCT 1900",age="119")
        fam1 = family("No1",  husband="No1",  wife="No2")
        indList = [indi1,indi2]
        famList = [fam1]
        a=gedHelper().listLargeAgeDifference(indList,famList)

        print(a)
        self.assertTrue(len(a)>0)
        
    #sb
    def test_recentBirthdays(self):
        indi1 = individual("No1", name="Child0 Jones", sex="M", birth="10 Nov 2019", )
        indi2 = individual("No2", name="Child1 Jones", sex="F", birth="19 Nov 2019")
        indi3 = individual("No3", name="Child3 Adams", sex="M", birth="22 Nov 2019")
        #extra child birthday not recent
        indi4 = individual("No4", name="Child4 Tu", sex="F", birth="11 Aug 2019")
        indList = [indi1,indi2,indi3,indi4]
        gedHelper().recentBirthdays(indList)

        
    def test_recentDeaths(self):
        indi1 = individual("No1", name="Child0 Jones", sex="M", death="10 Nov 2019", )
        indi2 = individual("No2", name="Child1 Jones", sex="F", death="19 Nov 2019")
        indi3 = individual("No3", name="Child3 Adams", sex="M", death="22 Nov 2019")
        #extra death not recent
        indi4 = individual("No4", name="Child4 Collins", sex="F", death="11 Aug 2019")
        indList = [indi1,indi2,indi3,indi4]
        gedHelper().recentDeaths(indList)
        
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
        self.assertFalse(indi2 not in output)

    #Na
    def test_Anniversary(self):
        anniversaries = []
        no_anniversary = []
        fam_1 = family("1", marDate = "31 DEC 2000")
        fam_2 = family("2", marDate = "1 JAN 2000")
        fam_3 = family("3")
        anniversaries.append(fam_1)
        no_anniversary.append(fam_2)
        no_anniversary.append(fam_3)
        # self.assertIsNotNone(gedHelper().Anniversary(anniversaries))
        self.assertIsNone(gedHelper().Anniversary(no_anniversary))

    def test_IllegitimateDates(self):
        self.assertEqual(gedUtil().getDate("30 FEB 2000"), "ERROR: INVALID DATE")
        self.assertNotEqual(gedUtil().getDate("1 JAN 2000"), "ERROR: INVALID DATE")
    
    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False)
