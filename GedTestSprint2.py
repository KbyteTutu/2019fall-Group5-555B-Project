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


        
    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False)
