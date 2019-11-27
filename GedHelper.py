__author__ = 'Group5'

# Basic programmed by Kt

import datetime
import copy

from GedMembers import Valid
from GedMembers import individual
from GedMembers import family
from GedUtil import gedUtil


class gedHelper(object):

    def __init__(self):
        pass

#Rx
    # US01 Date before CurrentDate
    def datebeforeCurrentdate(self, person):
        util = gedUtil()
        current = datetime.datetime.today().strftime('%d %b %Y')

        if (person.birth != "not mentioned"):
            return gedUtil().dateCompare(current, person.birth)
        elif (person.marDate != "not mentioned"):
            return gedUtil().dateCompare(person.marDate, current)
        elif (person.death != "not mentioned"):
            return gedUtil().dateCompare(person.death, current)
        elif (person.divDate != "not mentioned"):
            return gedUtil().dateCompare(person.divDate, current)
        else:
            return 0

    # US02 Birth before Marriage
    def birthBeforeMarriage(self, person):
        if (person.birth == "not mentioned")or(person.marDate == "not mentioned"):
            return True
        else:
            return gedUtil().dateCompare(person.marDate, person.birth)

#/Rx
#Kt
    # US03 Birth before death
    def birthBeforeDeath(self, person):
        if (person.birth == "not mentioned")or(person.death == "not mentioned"):
            return True
        else:
            return gedUtil().dateCompare(person.death, person.birth)

    # US04 Marriage before divorce
    def marriageBeforeDivorce(self, person):
        if (person.marDate == "not mentioned")or(person.divDate == "not mentioned"):
            return True
        else:
            return gedUtil().dateCompare(person.divDate, person.marDate)
#/Kt
#Sb
        # US05 Marriage before death
    def marriageBeforeDeath(self, person):
        if (person.marDate == "not mentioned")or(person.death == "not mentioned"):
            return True
        else:
            return gedUtil().dateCompare(person.death, person.marDate)

        # US06 Divorce before death

    def divorceBeforeDeath(self, person):
        if (person.divDate == "not mentioned")or(person.death == "not mentioned"):
            return True
        else:
            return gedUtil().dateCompare(person.death, person.divDate)
#/Sb
#Cs
    # US07 Less than 150 years old

    def lessThan150Years(self, person):
        return gedUtil.getAge(self, person) < 150

    # Does not work until implementation of FamilyC
    def validate_family(self, indList, famList):
        for family in famList:
            for ind in indList:
                for child in ind.familyC:
                    if(child == family.famid):
                        if ind.sex != 'M' and ind.sex != 'F':
                            return False
            if family.husband != "invalid/not mentioned" and family.husband.sex != 'M':
                return False
            if family.wife != "invalid/not mentioned" and family.wife.sex != 'F':
                return False

    # US08 Birth before marriage of parents
#/Cs
#Na
    # US09 Birth before death of parents
    def validBirth(self, indList, famList):
        return_flag = True
        util = gedUtil()
        for ind in indList:
            if ind.familyC != "not mentioned":
                father = None
                fatherID = None
                mother = None
                motherID = None
                fam = None
                marriage = None

                for family in famList:
                    if family.famid == ind.familyC:
                        fatherID = family.husband
                        motherID = family.wife
                        fam = family
                        break

                for inds in indList:
                    if inds.indi == fatherID:
                        father = inds
                        marriage = inds.marDate
                    if inds.indi == motherID:
                        mother = inds
                        marriage = inds.marDate

                try:
                    if util.getDate(father.death) is not None and util.getDate(father.death) < util.getDate(ind.birth) - datetime.timedelta(days=266):
                        print(
                            "Child is born more than 9 months after death of " + father.name)
                        return_flag = False

                    if util.getDate(mother.death) is not None and util.getDate(mother.death) < util.getDate(ind.birth):
                        print("Child is born after death of " + mother.name)
                        return_flag = False

                    if util.getDate(ind.birth) < util.getDate(marriage):
                        print("Child is born before marriage of " +
                              father.name + " and " + mother.name)
                        return_flag = False
                except:
                    print("")
        return return_flag

    # US10 Marriage after 14
    def validMarriage(self, indList, famList):
        return_flag = True
        util = gedUtil()
        current = datetime.datetime.today()
        min_birth = datetime.datetime(
            current.year - 14, current.month, current.day)

        for family in famList:
            husband = None
            wife = None
            for ind in indList:
                if ind.indi == family.husband:
                    husband = ind
                if ind.indi == family.wife:
                    wife = ind
                if husband is not None and wife is not None:
                    break

        try:
            if util.getDate(husband.birth) > min_birth:
                print(husband + " is married before 14 years old")
                return_flag = False

            if util.getDate(wife.birth) > min_birth:
                print(wife + " is married before 14 years old")
                return_flag = False
        except:
            print("")
        return return_flag
#/Na