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
    #Sprint2
    #Rh
    def test_nobigamy(self):
        indi1 = individual("No1", name="Zhang 1", wifeID="Zhang 1")
        indi2 = individual("No2", name="Zhang 2", husbID="Zhang 2")
        indi3 = individual("No3", name="Zhang 3", wifeID="Zhang 3")
        indi4 = individual("No4", name="Zhang 4", husbID="Zhang 4")
        fam1 = family("No1",  husband="Zhang 2",  wife="Zhang 1")
        fam2 = family("No2",  husband="Zhang 4", wife="Zhang 3")
        fam3 = family("No3",  husband="Zhang 4",  wife="Zhang 1")
        indList = [indi1,indi2,indi3,indi4]
        famList = [fam1,fam2,fam3]
        famListOrigin = copy.deepcopy(famList)
        gedHelper().nobigamy(indList,famList)

        self.assertTrue(famList == famListOrigin)

    def test_validParentsage(self):
        indi1 = individual("No1", name="Zhang 1", wifeID="Zhang 1", birth="10 OCT 1900")
        indi2 = individual("No2", name="Zhang 2", husbID="Zhang 2", birth="11 OCT 1900")
        indi3 = individual("No3", name="Zhang 3", familyC="Zhang 3", birth="10 OCT 1990")
        fam1 = family("No1",  husband="Zhang 2",  wife="Zhang 1")
        indList = [indi1,indi2,indi3]
        famList = [fam1]

        self.assertTrue(gedHelper().validParentsage(indList,famList) == "")
    
    #Kt
    def test_Siblings_spacing(self):
        indi1 = individual("No1", name="Zhang 1", birth="10 OCT 1900")
        indi2 = individual("No2", name="Zhang 2", birth="19 OCT 1900")
        indi3 = individual("No3", name="Zhang 3", birth="21 OCT 1900")
        indi4 = individual("No4", name="Zhang 4", birth="13 OCT 1901")
        indi5 = individual("No5", name="Zhang 5", birth="14 OCT 1902")
        fam1 = family("No1")
        fam2 = family("No2")
        fam1.children.append(indi1.indi)
        fam1.children.append(indi2.indi)
        fam1.children.append(indi3.indi)
        fam2.children.append(indi4.indi)
        fam2.children.append(indi5.indi)
        indList = [indi1,indi2,indi3]
        famList = [fam1]
        indList2 = [indi4,indi5]
        famList2 = [fam2]
        famListOrigin = copy.deepcopy(famList)
        famListOrigin2 = copy.deepcopy(famList2)

        famList = gedHelper().SiblingsSpacing(indList,famList)
        famList2 = gedHelper().SiblingsSpacing(indList2,famList2)
        self.assertFalse(famList == famListOrigin)
        self.assertTrue(famList2 == famListOrigin2)
    
    def test_MultipleBirthsDelete(self):
        indi1 = individual("No1", name="Zhang 1", birth="10 OCT 1900")
        indi2 = individual("No2", name="Zhang 2", birth="10 OCT 1900")
        indi3 = individual("No3", name="Zhang 3", birth="10 OCT 1900")
        indi4 = individual("No4", name="Zhang 4", birth="10 OCT 1900")
        indi5 = individual("No5", name="Zhang 5", birth="10 OCT 1900")
        #extra wrong birth
        indi6 = individual("No6", name="Zhang 6", birth="10 OCT 1900")
        fam1 = family("No1")
        fam1.children.append(indi1.indi)
        fam1.children.append(indi2.indi)
        fam1.children.append(indi3.indi)
        fam1.children.append(indi4.indi)
        fam1.children.append(indi5.indi)
        fam2 = family("No2")
        fam2.children.append(indi1.indi)
        fam2.children.append(indi2.indi)
        fam2.children.append(indi3.indi)
        fam2.children.append(indi4.indi)
        fam2.children.append(indi5.indi)
        fam2.children.append(indi6.indi)

        indList = [indi1,indi2,indi3,indi4,indi5,indi6]
        famList = [fam1,fam2]

        famListOrigin = copy.deepcopy(famList)
        famList = gedHelper().MultipleBirthsDelete(indList,famList)

        self.assertFalse(famList == famListOrigin)

    #Sb
    def test_MaleLastNames(self):
        indi1 = individual("No1", name="Husband1 Jones", sex="M", birth="10 OCT 1900", )
        indi2 = individual("No2", name="Child1 Jones", sex="M", familyC="Child1 Jones", birth="10 OCT 1930")
        indi3 = individual("No3", name="Husband2 Adams", sex="M", birth="11 OCT 1901")
        #extra wrong child last name
        indi4 = individual("No4", name="Child2 Tu", sex="M", familyC="Child2 Tu", birth="12 OCT 1932")
        
        fam1 = family("No1",  husband="Husband1 Jones", children="Child1 Jones")
        fam2 = family("No2",  husband="Husband2 Adams", children="Child2 Adams")
        indList = [indi1,indi2,indi3,indi4]
        famList = [fam1,fam2]
        self.assertTrue(gedHelper().MaleLastNames(indList,famList))
     
        
    
    def test_FewerSiblings(self):
    
        indi1 = individual("No1", name="Zhang 1", birth="11 OCT 1900")
        indi2 = individual("No2", name="Zhang 2", birth="12 OCT 1901")
        indi3 = individual("No3", name="Zhang 3", birth="13 OCT 1902")
        indi4 = individual("No4", name="Zhang 4", birth="14 OCT 1903")
        indi5 = individual("No5", name="Zhang 5", birth="15 OCT 1904")
        indi6 = individual("No5", name="Zhang 5", birth="16 OCT 1905")
        indi7 = individual("No5", name="Zhang 5", birth="17 OCT 1906")
        indi8 = individual("No5", name="Zhang 5", birth="18 OCT 1907")
        indi9 = individual("No5", name="Zhang 5", birth="19 OCT 1908")
        indi10 = individual("No5", name="Zhang 5", birth="20 OCT 1909")
        indi11 = individual("No5", name="Zhang 5", birth="21 OCT 1910")
        indi12 = individual("No5", name="Zhang 5", birth="22 OCT 1911")
        indi13 = individual("No5", name="Zhang 5", birth="23 OCT 1912")
        indi14 = individual("No5", name="Zhang 5", birth="24 OCT 1913")
        indi15 = individual("No5", name="Zhang 5", birth="25 OCT 1914")
        
        #extra wrong sibling (>15)
        indi16 = individual("No6", name="Zhang 6", birth="26 OCT 1915")
        
        fam1 = family("No1")
        fam1.children.append(indi1.indi)
        fam1.children.append(indi2.indi)
        fam1.children.append(indi3.indi)
        fam1.children.append(indi4.indi)
        fam1.children.append(indi5.indi)
        fam1.children.append(indi6.indi)
        fam1.children.append(indi7.indi)
        fam1.children.append(indi8.indi)
        fam1.children.append(indi9.indi)
        fam1.children.append(indi10.indi)
        fam1.children.append(indi11.indi)
        fam1.children.append(indi12.indi)
        fam1.children.append(indi13.indi)
        fam1.children.append(indi14.indi)
        fam1.children.append(indi15.indi)
        
        fam2 = family("No2")
        fam1.children.append(indi1.indi)
        fam1.children.append(indi2.indi)
        fam1.children.append(indi3.indi)
        fam1.children.append(indi4.indi)
        fam1.children.append(indi5.indi)
        fam1.children.append(indi6.indi)
        fam1.children.append(indi7.indi)
        fam1.children.append(indi8.indi)
        fam1.children.append(indi9.indi)
        fam1.children.append(indi10.indi)
        fam1.children.append(indi11.indi)
        fam1.children.append(indi12.indi)
        fam1.children.append(indi13.indi)
        fam1.children.append(indi14.indi)
        fam1.children.append(indi15.indi)
        fam1.children.append(indi16.indi)
        
        indList = [indi1,indi2,indi3,indi4,indi5,indi6,indi7,indi8,indi9,indi10,indi11,indi12,indi13,indi14,indi15,indi16]
        famList = [fam1,fam2]

        famListOrigin = copy.deepcopy(famList)
        famList = gedHelper().FewerSiblings(indList,famList)

    #Cs
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
        self.assertFalse(output == False)

    #Na
    def test_cousinsMarried(self):
        individuals = []
        families = []
        indi_1 = individual("1", name = "1", birth = "14 SEPT 1930", marrigeDate="14 SEPT 1950", family="2")
        indi_1.familyC = "1"
        indi_2 = individual("2", name ="2", birth = "15 SEPT 1930", marrigeDate="14 SEPT 1950", family="2")
        indi_2.familyC = "0"
        indi_3 = individual("3", name ="3", birth ="16 SEPT 1930", marrigeDate ="16 SEPT 1950", family="3")
        indi_3.familyC = "1"
        indi_4 = individual("4", name ="4", birth ="17 SEPT 1930", marrigeDate ="16 SEPT 1950", family="3")
        indi_4.familyC = "0"
        indi_5 = individual("5", name ="5", birth ="18 SEPT 1980", marrigeDate ="18 SEPT 2000", family="4")
        indi_5.familyC = "2"
        indi_6 = individual("6", name="6", birth ="19 SEPT 1980", marrigeDate ="18 SEPT 2000", family="4")
        indi_6.familyC = "3"
        individuals.append(indi_1)
        individuals.append(indi_2)
        individuals.append(indi_3)
        individuals.append(indi_4)
        individuals.append(indi_5)
        individuals.append(indi_6)
        fam_0 = family("0", children=["2", "4"])
        fam_1 = family("1", children=["1", "3"])
        fam_2 = family("2", husband="1", wife="2", children=["5"])
        fam_3 = family("3", husband="3", wife="4", children=["6"])
        fam_4 = family("4", husband="5", wife="6")
        families.append(fam_0)
        families.append(fam_1)
        families.append(fam_2)
        families.append(fam_3)
        families.append(fam_4)
        self.assertFalse(gedHelper().cousinsMarried(individuals,families))
        individuals = []
        families = []
        indi_1 = individual("1", name = "1", birth = "14 SEPT 1930", marrigeDate="14 SEPT 1950", family="2")
        indi_1.familyC = "1"
        indi_2 = individual("2", name ="2", birth = "15 SEPT 1930", marrigeDate="14 SEPT 1950", family="2")
        indi_2.familyC = "0"
        indi_3 = individual("3", name ="3", birth ="16 SEPT 1930", marrigeDate ="16 SEPT 1950", family="3")
        indi_3.familyC = "1"
        indi_4 = individual("4", name ="4", birth ="17 SEPT 1930", marrigeDate ="16 SEPT 1950", family="3")
        indi_4.familyC = "0"
        individuals.append(indi_1)
        individuals.append(indi_2)
        individuals.append(indi_3)
        individuals.append(indi_4)
        fam_0 = family("0", children=["2", "4"])
        fam_1 = family("1", children=["1", "3"])
        fam_2 = family("2", husband="1", wife="2")
        fam_3 = family("3", husband="3", wife="4")
        families.append(fam_0)
        families.append(fam_1)
        families.append(fam_2)
        families.append(fam_3)
        self.assertFalse(gedHelper().cousinsMarried(individuals,families))

    def test_AuntsAndUncles(self):
        individuals = []
        families = []
        indi_1 = individual("1", name = "1", birth = "14 SEPT 1930", marrigeDate="14 SEPT 1950", family="2")
        indi_1.familyC = "1"
        indi_2 = individual("2", name ="2", birth = "15 SEPT 1930", marrigeDate="14 SEPT 1950", family="2")
        indi_2.familyC = "0"
        indi_3 = individual("3", name ="3", birth ="16 SEPT 1930", marrigeDate ="16 SEPT 1950", family="3")
        indi_3.familyC = "1"
        indi_4 = individual("4", name ="4", birth ="17 SEPT 1930", marrigeDate ="16 SEPT 1950", family="3")
        indi_4.familyC = "0"
        indi_5 = individual("5", name ="5", birth ="18 SEPT 1980", marrigeDate ="18 SEPT 2000", family="4")
        indi_5.familyC = "2"
        indi_6 = individual("6", name="6", birth ="19 SEPT 1980", marrigeDate ="18 SEPT 2000", family="4")
        indi_6.familyC = "0"
        individuals.append(indi_1)
        individuals.append(indi_2)
        individuals.append(indi_3)
        individuals.append(indi_4)
        individuals.append(indi_5)
        individuals.append(indi_6)
        fam_0 = family("0", children=["2", "4", "6"])
        fam_1 = family("1", children=["1", "3"])
        fam_2 = family("2", husband="1", wife="2", children=["5"])
        fam_3 = family("3", husband="3", wife="4")
        fam_4 = family("4", husband="5", wife="6")
        families.append(fam_0)
        families.append(fam_1)
        families.append(fam_2)
        families.append(fam_3)
        families.append(fam_4)
        self.assertFalse(gedHelper().AuntsAndUncles(individuals,families))
        individuals = []
        families = []
        indi_1 = individual("1", name = "1", birth = "14 SEPT 1930", marrigeDate="14 SEPT 1950", family="2")
        indi_1.familyC = "1"
        indi_2 = individual("2", name ="2", birth = "15 SEPT 1930", marrigeDate="14 SEPT 1950", family="2")
        indi_2.familyC = "0"
        indi_3 = individual("3", name ="3", birth ="16 SEPT 1930", marrigeDate ="16 SEPT 1950", family="3")
        indi_3.familyC = "1"
        indi_4 = individual("4", name ="4", birth ="17 SEPT 1930", marrigeDate ="16 SEPT 1950", family="3")
        indi_4.familyC = "0"
        individuals.append(indi_1)
        individuals.append(indi_2)
        individuals.append(indi_3)
        individuals.append(indi_4)
        fam_0 = family("0", children=["2", "4"])
        fam_1 = family("1", children=["1", "3"])
        fam_2 = family("2", husband="1", wife="2")
        fam_3 = family("3", husband="3", wife="4")
        families.append(fam_0)
        families.append(fam_1)
        families.append(fam_2)
        families.append(fam_3)
        self.assertFalse(gedHelper().AuntsAndUncles(individuals,families))


        
    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False)
