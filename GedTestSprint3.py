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
    #Sprint3
    def test_correctGender(self):
        indi1 = individual("No1", name="Zhang 1", wifeID="Zhang 1", sex="F")
        indi2 = individual("No2", name="Zhang 2", husbID="Zhang 2", sex="M")
        indi3 = individual("No3", name="Zhang 3", wifeID="Zhang 3", sex="F")
        indi4 = individual("No4", name="Zhang 4", husbID="Zhang 4", sex="F")
        fam1 = family("No1",  husband="Zhang 2",  wife="Zhang 1")
        fam2 = family("No2",  husband="Zhang 4", wife="Zhang 3")
        indList = [indi1,indi2,indi3,indi4]
        famList = [fam1,fam2]
        output = gedHelper().correctGender(indList,famList)
        self.assertTrue(output == indList)



    def test_noUnique_IDs(self):
        indi1 = individual("No1", name="Zhang 1", wifeID="Zhang 1", birth="10 OCT 1900")
        indi2 = individual("No2", name="Zhang 2", husbID="Zhang 2", birth="11 OCT 1900")
        indi3 = individual("No1", name="Zhang 3", familyC="Zhang 3", birth="10 OCT 1990")
        fam1 = family("No1",  husband="Zhang 2",  wife="Zhang 1")
        fam2 = family("No1",  husband="Zhang 4", wife="Zhang 3")
        indList = [indi1,indi2,indi3]
        famList = [fam1,fam2]
        output = gedHelper().noUnique_IDs(indList)
        output2 = gedHelper().noUnique_famIDs(famList)
        self.assertTrue(output == indList)
        self.assertTrue(output2 == famList)
    
    #Kt
    def test_UniqueNameAndBirth(self):
        indi1 = individual("No1", name="same", birth="10 OCT 1900")
        indi2 = individual("No2", name="same", birth="10 OCT 1900")
        indi3 = individual("No3", name="different", birth="11 OCT 1900")

        indList1 = [indi1,indi2]
        indList2 = [indi1,indi3]

        self.assertTrue(len(gedHelper().UniqueNameAndBirth(indList1))== 1)
        self.assertTrue(len(gedHelper().UniqueNameAndBirth(indList2))== 2)
    
    def test_UniqueFamily(self):
        fam1 = family("No1",  husband="a_hus",  wife="a_wife")
        fam2 = family("No2",  husband="a_hus", wife="a_wife")
        fam3 = family("No3",  husband="b", wife="b")

        famList = [fam1,fam2]
        famListDifferent = [fam1,fam2,fam3]

        self.assertTrue(len(gedHelper().UniqueFamily(famList))== 1)
        self.assertTrue(len(gedHelper().UniqueFamily(famListDifferent))== 2)
    #Sb
    def test_UniqueChildName(self):
        indi1 = individual("No1", name="Child1 Jones", familyC="Child1 Jones",birth='10 OCT 1900')
        indi2 = individual("No2", name="Child2 Jones", familyC="Child2 Jones", birth='10 OCT 1901')
        indi3 = individual("No3", name="Child3 Adams", familyC="Child3 Adams", birth='11 OCT 1901')
        #extra same child first name
        indi4 = individual("No4", name="Child3 Adams", familyC="Child3 Adams", birth='12 OCT 1901')
        
        fam1 = family("No1")
        fam1.children.append(indi1.indi)
        fam1.children.append(indi2.indi)
        fam2 = family("No2")
        fam1.children.append(indi3.indi)
        fam1.children.append(indi4.indi)
        
        indList = [indi1,indi2,indi3,indi4]
        famList = [fam1,fam2]
        self.assertTrue(gedHelper().UniqueChildName(indList,famList))


        # He doesn't have time to correct this.
       
    def test_listBirths(self):
        individuals = []
        
        indi_1 = individual("1", name = "Test", birth = "14 SEPT 1996", family="1")
        indi_2 = individual("2", name = "Test2", birth = "15 SEPT 1996",family="1")
        indi_3 = individual("3", name = "Test3", birth = "16 SEPT 2019" ,family="2")
        individuals.append(indi_1)
        individuals.append(indi_2)
        individuals.append(indi_3)
        
        self.assertEqual(individuals, gedHelper().listBirths(individuals))
    #Cs
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
        gedHelper().orderSibling(indList1, fam1)

    #Na
    def test_ListDeceased(self):
        individuals = []
        dead = []
        indi_1 = individual("1", name = "Test", birth = "14 SEPT 1996", death = "14 SEPT 2019", marrigeDate="14 SEPT 2018", family="1")
        indi_2 = individual("2", name = "Test2", birth = "15 SEPT 1996", death = "15 SEPT 2019", marrigeDate="14 SEPT 2018", family="1")
        indi_3 = individual("3", name = "Test3", birth = "16 SEPT 2019")
        individuals.append(indi_1)
        individuals.append(indi_2)
        individuals.append(indi_3)
        dead.append(indi_1)
        dead.append(indi_2)
        self.assertNotEqual(individuals, gedHelper().listDeceased(individuals))
        self.assertEqual(dead, gedHelper().listDeceased(individuals))

    def test_LivingMarried(self):
        individuals = []
        families = []
        living = []
        indi_1 = individual("1", name = "Test", birth = "14 SEPT 1996", death = "14 SEPT 2019", marrigeDate="14 SEPT 2018", family="1")
        indi_2 = individual("2", name = "Test2", birth = "15 SEPT 1996", death = "15 SEPT 2019", marrigeDate="14 SEPT 2018", family="1")
        indi_3 = individual("3", name = "Test3", birth = "16 SEPT 1996", marrigeDate="16 SEPT 2018", family="2")
        indi_4 = individual("4", name = "Test4", birth = "17 SEPT 1996", marrigeDate="16 SEPT 2018", family="2")
        individuals.append(indi_1)
        individuals.append(indi_2)
        individuals.append(indi_3)
        individuals.append(indi_4)
        living.append(indi_3)
        living.append(indi_4)
        fam_1 = family("1", husband="1", wife="2", marDate="14 SEPT 2018")
        fam_2 = family("2", husband="3", wife="4", marDate="16 SEPT 2018")
        families.append(fam_1)
        families.append(fam_2)
        # self.assertEqual(living, gedHelper().livingMarried(individuals,families))
        self.assertNotEqual(individuals, gedHelper().livingMarried(individuals,families))


    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False)
