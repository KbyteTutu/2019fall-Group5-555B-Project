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

    def test_MaleLastNames(self):
        indi1 = individual("No1", name="Husband1 Jones", sex="M", birth="10 OCT 1900", )
        indi2 = individual("No2", name="Child1 Jones", sex="M", familyC="Child1 Jones", birth="10 OCT 1930")
        indi3 = individual("No3", name="Husband2 Adams", sex="M", birth="11 OCT 1901")
        #extra wrong child last name
        indi4 = individual("No4", name="Child2 Tu", sex="M", familyC="Child2 Adams", birth="12 OCT 1932")
        
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
         
    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False)
