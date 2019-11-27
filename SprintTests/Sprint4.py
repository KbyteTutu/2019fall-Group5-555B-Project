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

    def test_recentBirthdays(self):
        indi1 = individual("No1", name="Child0 Jones", sex="M", birth="10 Nov 2019", )
        indi2 = individual("No2", name="Child1 Jones", sex="F", birth="19 Nov 2019")
        indi3 = individual("No3", name="Child3 Adams", sex="M", birth="22 Nov 2019")
        #extra child birthday not recent
        indi4 = individual("No4", name="Child4 Tu", sex="F", birth="11 Aug 2019")
        indList = [indi1,indi2,indi3,indi4]
        self.assertTrue(gedHelper().recentBirthdays(indList))
        
    def test_recentDeaths(self):
        indi1 = individual("No1", name="Child0 Jones", sex="M", death="10 Nov 2019", )
        indi2 = individual("No2", name="Child1 Jones", sex="F", death="19 Nov 2019")
        indi3 = individual("No3", name="Child3 Adams", sex="M", death="22 Nov 2019")
        #extra death not recent
        indi4 = individual("No4", name="Child4 Collins", sex="F", death="11 Aug 2019")
        indList = [indi1,indi2,indi3,indi4]
        self.assertTrue(gedHelper().recentDeaths(indList)) 
         
    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False)
