import unittest
import GedRead
from GedMembers import Valid
from GedMembers import individual
from GedMembers import family
from GedHelper import gedHelper
from GedUtil import gedUtil


# from pytest import ExitCode

class test_ged(unittest.TestCase):

    def test_validBirth(self):
        individuals = []
        families = []
        indi_1 = individual("1", name = "Test", birth = "14 SEPT 1996", death = "14 SEPT 2019", marrigeDate="14 SEPT 2018", family="1")
        indi_2 = individual("2", name = "Test2", birth = "15 SEPT 1996", death = "15 SEPT 2019", marrigeDate="14 SEPT 2018", family="1")
        indi_3 = individual("3", name = "Test3", birth = "16 SEPT 2019")
        indi_3.familyC = "1"
        individuals.append(indi_1)
        individuals.append(indi_2)
        individuals.append(indi_3)
        fam_1 = family("1", husband= "1", wife= "2", children= ["3"], marDate= "14 SEPT 2018")
        families.append(fam_1)
        self.assertFalse(gedHelper().validBirth(individuals,families))
        individuals.pop()
        families.pop()
        indi_4 = individual("3", name = "Test3", birth = "16 SEPT 2018")
        indi_4.familyC = "1"
        individuals.append(indi_4)
        fam_2 = family("1", husband= "1", wife= "2", children= ["3"], marDate= "14 SEPT 2018")
        families.append(fam_2)
        self.assertTrue(gedHelper().validBirth(individuals,families))
        
    def test_validMarriage(self):
        individuals = []
        families = []
        indi_1 = individual("1", name = "Test", birth = "14 SEPT 1996", death = "14 SEPT 2019", marrigeDate="14 SEPT 2018", family="1")
        indi_2 = individual("2", name = "Test2", birth = "15 SEPT 2017", death = "15 SEPT 2019", marrigeDate="14 SEPT 2018", family="1")
        individuals.append(indi_1)
        individuals.append(indi_2)
        fam_1 = family("1", husband= "1", wife= "2", marDate= "14 SEPT 2018")
        families.append(fam_1)
        self.assertFalse(gedHelper().validMarriage(individuals,families))
        individuals.pop()
        families.pop()
        indi_4 = individual("2", name = "Test2", birth = "15 SEPT 1996", death = "15 SEPT 2019", marrigeDate="14 SEPT 2018", family="1")
        individuals.append(indi_4)
        fam_2 = family("1", husband= "1", wife= "2", marDate= "14 SEPT 2018")
        families.append(fam_2)
        self.assertTrue(gedHelper().validMarriage(individuals,families))

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
        self.assertTrue(gedHelper().cousinsMarried(individuals,families))

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
        self.assertTrue(gedHelper().AuntsAndUncles(individuals,families))

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
        self.assertEqual(living, gedHelper().livingMarried(individuals,families))
        self.assertNotEqual(individuals, gedHelper().livingMarried(individuals,families))
        
    # Change Anniversary in GedHelper to return anniversaries
    def test_Anniversary(self):
        anniversaries = []
        no_anniversary = []
        fam_1 = family("1", marDate = "31 DEC 2000")
        fam_2 = family("2", marDate = "1 JAN 2000")
        fam_3 = family("3")
        anniversaries.append(fam_1)
        no_anniversary.append(fam_2)
        no_anniversary.append(fam_3)
        self.assertIsNotNone(gedHelper().Anniversary(anniversaries))
        self.assertIsNone(gedHelper().Anniversary(no_anniversary))

    def test_IllegitimateDates(self):
        self.assertEqual(gedUtil().getDate("30 FEB 2000"), "ERROR: INVALID DATE")
        self.assertNotEqual(gedUtil().getDate("1 JAN 2000"), "ERROR: INVALID DATE")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False)