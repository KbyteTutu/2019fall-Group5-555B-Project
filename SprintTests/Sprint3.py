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
    
    
    #Sb

    def test_UniqueChildName(self):
        indi1 = individual("No1", name="Child1 Jones", familyC="Child1 Jones" birth="10 OCT 1900", )
        indi2 = individual("No2", name="Child2 Jones", familyC="Child2 Jones", birth="10 OCT 1901")
        indi3 = individual("No3", name="Child3 Adams", familyC="Child3 Adams", birth="11 OCT 1901")
        #extra same child first name
        indi4 = individual("No4", name="Child3 Adams", familyC="Child3 Adams", birth="12 OCT 1901")
        
        fam1 = family("No1")
        fam1.children.append(indi1.indi)
        fam1.children.append(indi2.indi)
        fam2 = family("No2")
        fam1.children.append(indi3.indi)
        fam1.children.append(indi4.indi)
        
        indList = [indi1,indi2,indi3,indi4]
        famList = [fam1,fam2]
        self.assertTrue(gedHelper().UniqueChildName(indList,famList))
       
    def test_listBirths(self):
        individuals = []
        
        indi_1 = individual("1", name = "Test", birth = "14 SEPT 1996", family="1")
        indi_2 = individual("2", name = "Test2", birth = "15 SEPT 1996",family="1")
        indi_3 = individual("3", name = "Test3", birth = "16 SEPT 2019" family="2")
        individuals.append(indi_1)
        individuals.append(indi_2)
        individuals.append(indi_3)
        
        self.assertEqual(individuals, gedHelper().listBirths(individuals))
        
  
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False)
