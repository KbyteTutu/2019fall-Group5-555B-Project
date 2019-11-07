__author__= 'Group5'

import datetime
from GedMembers import Valid
from GedMembers import individual
from GedMembers import family
from GedUtil import gedUtil

class gedHelper(object):


    def __init__(self):
        pass
    #US01 Date before CurrentDate
    def datebeforeCurrentdate(self, person):
        util = gedUtil()
        current = datetime.datetime.today()
        if (person.birth !="not mentioned"):
            return gedUtil().dateCompare(getDate(current),person.birth)
        elif (person.marDate !="not mentioned"):
            return gedUtil().dateCompare(person.marDate,getDate(current))
        elif (person.death !="not mentioned"):
            return gedUtil().dateCompare(person.death,getDate(current))
        elif (person.divDate !="not mentioned"):
            return gedUtil().dateCompare(person.divDate,getDate(current))
        else:
            return 0
    
    #US02 Birth before Marriage
    def birthBeforeMarriage(self, person):
        if (person.birth =="not mentioned")or(person.marDate =="not mentioned"):
            return 0
        else:
            return gedUtil().dateCompare(person.marDate,person.birth)

    #US03 Birth before death
    def birthBeforeDeath(self, person):
        if (person.birth =="not mentioned")or(person.death =="not mentioned"):
            return 0
        else:
            return gedUtil().dateCompare(person.death,person.birth)
        
    #US04 Marriage before divorce
    def marriageBeforeDivorce(self, person):
        if (person.marDate =="not mentioned")or(person.divDate =="not mentioned"):
            return 0
        else:
            return gedUtil().dateCompare(person.divDate,person.marDate)

    #US07 Less than 150 years old
    def lessThan150Years(self, person):
        return gedUtil.getAge(self, person) < 150

    def validate_family(self,indList,famList):
        for family in famList:
            for ind in indList:
                if(ind.familyC== family.famid):
                    if ind.sex != 'M' and ind.sex != 'F':
                        return False
            if family.husband != "invalid/not mentioned" and family.husband.sex != 'M':
                return False
            if family.wife != "invalid/not mentioned" and family.wife.sex != 'F':
                return False

    #US09 Birth before death of parents
    def validBirth(self,indList, famList):
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

                if util.getDate(father.death) is not None and util.getDate(father.death) < util.getDate(ind.birth) - datetime.timedelta(days=266):
                    print("Child is born more than 9 months after death of father")
                    return_flag = False

                if util.getDate(mother.death) is not None and util.getDate(mother.Death) < util.getDate(ind.birth):
                    print("Child is born after death of mother")
                    return_flag = False

                if util.getDate(ind.birth) < util.getDate(marriage):
                    print("Child is born before marriage of parents")
                    return_flag = False
        return return_flag

    #US10 Marriage after 14
    def validMarriage(self,indList, famList):
        return_flag = True
        util = gedUtil()
        current = datetime.datetime.today()
        min_birth = datetime.datetime(current.year - 14, current.month, current.day)

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

            if util.getDate(husband.birth) > min_birth:
                print(husband + " is married before 14 years old")
                return_flag = False
            
            if util.getDate(wife.birth) > min_birth:
                print(wife + " is married before 14 years old")
                return_flag = False

        return return_flag

    #US29 List Deceased
    def listDeceased(self,indList):
        deceased = []
        for ind in indList:
            if ind.death != "not mentioned":
                deceased.append(ind)
        return deceased

    #US30 List living married
    def livingMarried(self,indList,famList):
        living = []
        for family in famList:
            husband_id = family.husband
            wife_id = family.wife
            husband = None
            wife = None

            for ind in indList:
                if ind.indi == husband_id and ind.death != "not mentioned":
                    husband = ind
                if ind.indi == wife_id and ind.death != "not mentioned":
                    wife = ind
            if wife is not None and husband is not None:
                living.append(wife)
                living.append(husband)
        return living


    
 
