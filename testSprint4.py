# -*- coding: utf-8 -*-

import unittest
import GedRead
from GedMembers import Valid
from GedMembers import individual
from GedMembers import family
from GedHelper import gedHelper
from GedUtil import gedUtil


# from pytest import ExitCode

class test_ged(unittest.TestCase):

    def test_livingsingle(self):
        indi1 = individual("No1", name="Zhang 1", wifeID="Zhang 1", birth="10 OCT 1999", marrigeDate="10 OCT 2010", death="")
        indi2 = individual("No2", name="Zhang 2", husbID="Zhang 2", birth="10 OCT 1998", marrigeDate="10 OCT 2010", death="")
        indi3 = individual("No3", name="Zhang 3", wifeID="Zhang 3", birth="10 OCT 1997", marrigeDate="10 OCT 2010", death="")
        indi4 = individual("No4", name="Zhang 4", husbID="Zhang 4", birth="10 OCT 1996", marrigeDate="10 OCT 2010", death="")
        indi5 = individual("No5", name="Zhang 5", birth="10 OCT 1970", death="")
        indList = [indi1,indi2,indi3,indi4,indi5]
        gedHelper().livingsingle(indList)

    def test_multiplebirths(self):
        indi1 = individual("No1", name="Zhang 1", wifeID="Zhang 1", birth="10 OCT 1900")
        indi2 = individual("No2", name="Zhang 2", husbID="Zhang 2", birth="10 OCT 1900")
        indi3 = individual("No3", name="Zhang 3", familyC="Zhang 3", birth="10 OCT 1990")
        fam1 = family("No1",  husband="Zhang 2",  wife="Zhang 1", children="Zhang 3")
        indList = [indi1,indi2,indi3]
        famList = [fam1]
        self.assertTrue(gedHelper().multiplebirths(indList,famList))


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False)