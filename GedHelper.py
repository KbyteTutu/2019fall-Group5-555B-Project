__author__ = 'Group5'


import datetime
import copy
from GedMembers import Valid
from GedMembers import individual
from GedMembers import family
from GedUtil import gedUtil


class gedHelper(object):

    def __init__(self):
        pass
    # US01 Date before CurrentDate

    def datebeforeCurrentdate(self, person):
        util = gedUtil()
        current = datetime.datetime.today()
        if (person.birth != "not mentioned"):
            return gedUtil().dateCompare(util.getDate(current), person.birth)
        elif (person.marDate != "not mentioned"):
            return gedUtil().dateCompare(person.marDate, util.getDate(current))
        elif (person.death != "not mentioned"):
            return gedUtil().dateCompare(person.death, util.getDate(current))
        elif (person.divDate != "not mentioned"):
            return gedUtil().dateCompare(person.divDate, util.getDate(current))
        else:
            return 0

    # US02 Birth before Marriage
    def birthBeforeMarriage(self, person):
        if (person.birth == "not mentioned")or(person.marDate == "not mentioned"):
            return True
        else:
            return gedUtil().dateCompare(person.marDate, person.birth)

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
                    print("incomplete info")
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
            print("incomplete data")
        return return_flag

    # US11 No bigamy
    def nobigamy(self,indList,famList) -> list:
        outputindList = copy.deepcopy(famList)
        for ind in indList:
            husbandchecklist = []
            wifechecklist = []
            husbandchecklist.append(ind.husbID)
            wifechecklist.append(ind.wifeID)
        husbandchecklist = set(husbandchecklist)
        wifechecklist = set(wifechecklist)
        for fam in famList:
            count = 0
            for check in husbandchecklist:
                if fam.husband == check:
                    count +=1
                if count >0:
                 outputindList.remove(fam)
        for fam in famList:
            count = 0
            for check in wifechecklist:
                if fam.husband == check:
                    count += 1
                if count > 0:
                    outputindList.remove(fam)
        return outputindList

    # US12 Parents not too old
    def validParentsage(self, indList, famList):
        return_flag = True
        util = gedUtil()

        for family in famList:
            husband = None
            wife = None
            children = None
            for ind in indList:
                if ind.indi == family.husband:
                    husband = ind
                if ind.indi == family.wife:
                    wife = ind
                if ind.indi == family.children:
                    children == ind
                if husband is not None and wife is not None and children is not None:
                    break

        try:
            if (util.getAge(husband.birth) - util.getAge(children.birth)) > 80:
                print("Parent of father is too old")
                return_flag = False

            if (gedUtil.getAge(wife.birth) - gedUtil.getAge(children.birth)) > 60:
                print("Parent of mother is too old")
                return_flag = False
        except:
            print("Wrong data")
        return return_flag

    #US13 Siblings spacing
    def SiblingsSpacing(self,indList,famList):
        util = gedUtil()
        outputindList = copy.deepcopy(famList)
        for fam in famList:
            childBirthList = []
            if fam.children.count >= 0: 
                for child in fam.children:
                    birthStr = util.getBirthStrByIndi(child,indList)
                    if birthStr != "not mentioned":
                        childBirthList.append(util.getDate(birthStr))
            for Date in childBirthList:
                for Date2 in childBirthList:
                    if gedHelper().SiblingsSpacingUtil(Date,Date2):
                        outputindList.remove(fam)
                        break
        return outputindList
    
    def SiblingsSpacingUtil(self,date1,date2):
        d = date1-date2
        d = abs(d)
        if (d.days>2) and (d.days<240):
            return True # this means wrong info
        else:
            return False

    #US14 Multiple births <= 5
    def MultipleBirthsDelete(self,indList,famList):
        util = gedUtil()
        outputindList = copy.deepcopy(famList)
        for fam in famList:
            childBirthList = []
            if fam.children.count >= 5: # only consider this situation
                for child in fam.children:
                    birthStr = util.getBirthStrByIndi(child,indList)
                    if birthStr != "Not Mentioned":
                        childBirthList.append(birthStr)
            if childBirthList.count > 5 : # valid record more than 4
                for item in childBirthList:
                    if childBirthList.count(item)>5:
                        outputindList.remove(fam)
                        break
        return outputindList

    #US17 No marriage to descendants
    def marriageToDescendant(self, indList, famList):
        for ind in indList:
            if ind.family != "not mentioned":
                for family in famList:
                    fatherID = []
                    motherID = []
                    descendantID = []
                    for ind in ind.family:
                        if family.famid == ind.family:
                            fatherID.append(family.husband)
                            motherID.append(family.wife)
                            descendantID.append(ind)
                    for ind in descendantID:
                        for i in fatherID:
                            if ind.husbID == i:
                                print(ind + " is married to an ancestor")
                                return False
                        for i in motherID:
                            if ind.wifeID == i:
                                print(ind + " is married to an ancestor")
                                return False
        return True

    #US18 Siblings should not marry
    def siblingsMarried(self, indList, famList):
        for fam in famList:
            childrenList = []
            for ind in indList:
                for child in fam.children:
                    if ind.indi == child:
                        childrenList.append(ind)
            for i in childrenList:
                for j in childrenList:
                    if (i.husbID == j.indi or i.wifeID == j.indi or i.indi == j.husbID or i.indi == j.wifeID):
                        print(i + " and " + j + " are married siblings.")
                        return False
        return True



    #US19 First Cousins Should Not Marry to be continued
    def cousinsMarried(self,indList,famList):
        return_flag = True
        util = gedUtil()

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

    # US20 Aunts and Uncles to be continued

    # US21 Correct gender for role
        def correctGender(self, indList, famList):
            return_flag = True

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
                if (husband.sex) != "M":
                    print(husband + "should be Male")
                    husband.sex = "M"
                    return_flag = False
                if (wife.sex) != "F":
                    print(wife + "should be Female")
                    wife.sex = "F"
                    return_flag = False
            except:
                print("incomplete data")
            return return_flag

    # US22 Unique IDs
    def noUnique_IDs(self,indList) -> list:
        for ind in indList:
            Idlist = []
            Idlist.append(ind.indi)
        checklist = set(Idlist)
        for id_check in checklist:
            count = 0
            for id_checks in Idlist:
                if id_check == id_checks:
                    count +=1
            if count > 0:
                nouniquelist = []
                nouniquelist.append(id_check)
        return nouniquelist

    def MultipleidsDelete(self,nouniquelist,indList) ->list:
        checklist = nouniquelist
        for ind in indList:
            count = 1
            for id_checks in checklist:
                if ind.indi == id_checks:
                        count += 1
                if count > 1:
                    indlist.remove(ind)
        return indlist

    #US23 Unique name and birth date
    # I overide the __hash__ and __eq__ to implement this.
    def UniqueNameAndBirth(self,indList):
        return set(indList)

    #US24 Unique families by spouses
    def UniqueFamily(self,famList):
        return set(famList)


    #US29 List Deceased
    def listDeceased(self,indList):
        deceased = []
        for ind in indList:
            if ind.death != "not mentioned":
                deceased.append(ind)
        return deceased

    # US30 List living married
    def livingMarried(self, indList, famList):
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
