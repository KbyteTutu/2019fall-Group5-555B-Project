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

# Rx
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

# /Rx
# Kt
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
# /Kt
# Sb
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
# /Sb
# Cs
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
# /Cs
# Na
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
                    pass
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
            pass
        return return_flag
# /Na


# Sprint2

# Rh
    # US11 No bigamy

    def nobigamy(self, indList, famList) -> list:
        outputindList = copy.deepcopy(famList)
        husbandchecklist = []
        wifechecklist = []
        for ind in indList:
            husbandchecklist.append(ind.husbID)
            wifechecklist.append(ind.wifeID)
        husbandchecklist = set(husbandchecklist)
        wifechecklist = set(wifechecklist)
        for fam in famList:
            count = 0
            for check in husbandchecklist:
                if fam.husband == check:
                    count += 1
                if count > 1:
                    if fam in outputindList:
                        outputindList.remove(fam)
        for fam in famList:
            count = 0
            for check in wifechecklist:
                if fam.husband == check:
                    count += 1
                if count > 1:
                    if fam in outputindList:
                        outputindList.remove(fam)
        return outputindList

    # US12 Parents not too old
    def validParentsage(self, indList, famList):
        return_str = ""
        util = gedUtil()

        for family in famList:
            temp = individual("Temp", name="Temp")
            husband = individual("Temp", name="Temp")
            wife = individual("Temp", name="Temp")
            children = individual("Temp", name="Temp")
            for ind in indList:
                if ind.indi == family.husband:
                    husband = ind
                if ind.indi == family.wife:
                    wife = ind
                if ind.indi == family.children:
                    children == ind
                if husband is not None and wife is not None and children is not None:
                    break
            if husband != temp:
                if (util.getAge(husband.birth) - util.getAge(children.birth)) > 80:
                    return_str += family.famid + "- father is too old\r\n"
            if wife != temp:
                if (util.getAge(wife.birth) - util.getAge(children.birth)) > 60:
                    return_str += family.famid + "- mother is too old\r\n"

            return return_str
# /#Rh

# Kt

    # US13 Siblings spacing
    def SiblingsSpacing(self, indList, famList):
        util = gedUtil()
        outputFam = copy.deepcopy(famList)
        for fam in famList:
            childBirthList = []
            if len(fam.children) >= 0:
                for child in fam.children:
                    birthStr = util.getBirthStrByIndi(child, indList)
                    if birthStr != "not mentioned":
                        childBirthList.append(util.getDate(birthStr))
            for Date in childBirthList:
                for Date2 in childBirthList:
                    if gedHelper().SiblingsSpacingUtil(Date, Date2):
                        if fam in outputFam:
                            outputFam.remove(fam)
                            print(fam.famid+"- Siblings spacing ")
                            break
        return outputFam

    def SiblingsSpacingUtil(self, date1, date2):
        d = date1-date2
        d = abs(d)
        if (d.days > 2) and (d.days < 240):
            return True  # this means wrong info
        else:
            return False

    # US14 Multiple births <= 5
    def MultipleBirthsDelete(self, indList, famList):
        util = gedUtil()
        outputindList = copy.deepcopy(famList)
        for fam in famList:
            childBirthList = []

            if len(fam.children) >= 5:  # only consider this situation
                for child in fam.children:
                    birthStr = util.getBirthStrByIndi(child, indList)
                    if birthStr != "Not Mentioned":
                        childBirthList.append(birthStr)
            if len(childBirthList) > 5:  # valid record more than 4
                for item in childBirthList:
                    if childBirthList.count(item) > 5:
                        outputindList.remove(fam)
                        print(fam.famid+"- Multiple births >5 ")
                        break
        return outputindList

# /Kt

# Sb
    def FewerSiblings(self, indList, famList):
        util = gedUtil()
        outputindList = copy.deepcopy(famList)
        for fam in famList:
            if fam.children.count > 15:
                outputindList.remove(fam)
        return outputindList

        # US16 Male Last Names
    def MaleLastNames(self, indList, famList):
        util = gedUtil()
        outputindList = copy.deepcopy(famList)
        husband = None
        child = None
        for family in famList:
            for ind in indList:
                if ind.indi == family.husband:
                    husband = ind
                    lastName = husband.name.split()[1]
                    for child in family.children:
                        for ind in indList:
                            if ind.indi == family.children:
                                child = ind
                                if (child.sex == "M") and (child.name.split()[1] != lastName):
                                    outputindList.remove(family)
        return outputindList
# Sb

# Cs
    # US17 No marriage to descendants
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
                        for i in motherID:
                            if ind.wifeID == i:
                                print(ind + " is married to an ancestor")

    # US18 Siblings should not marry

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

# /Cs
# Na
    # US19 First Cousins Should Not Marry

    def cousinsMarried(self, indList, famList):
        return_flag = True
        TempNoneIndi = individual("temp")

        for family in famList:
            # Get the couple's IDs
            husband = TempNoneIndi
            wife = TempNoneIndi
            for ind in indList:
                if ind.indi == family.husband:
                    husband = ind
                if ind.indi == family.wife:
                    wife = ind
                if husband is not TempNoneIndi and wife is not TempNoneIndi:
                    break

            # Get the parents' IDs
            husband_mother = TempNoneIndi
            husband_father = TempNoneIndi
            wife_mother = TempNoneIndi
            wife_father = TempNoneIndi
            for child_fam in famList:
                if husband.indi in child_fam.children:
                    husband_mother = child_fam.wife
                    husband_father = child_fam.husband
                if wife.indi in child_fam.children:
                    wife_mother = child_fam.wife
                    wife_father = child_fam.husband
                if husband_mother is not TempNoneIndi and wife_mother is not TempNoneIndi:
                    break

            try:
                # Husband's mother is a sister to one of the wife's parents
                if husband_mother.familyC == wife_mother.familyC or husband_mother.familyC == wife_father.familyC:
                    print(family.famid + "- First Cousins Should Not Marry")
                    return_flag = False

            # Husband's father is a brother to one of the wife's parents
                if husband_father.familyC == wife_mother.familyC or husband_father.familyC == wife_father.familyC:
                    print(family.famid + "- First Cousins Should Not Marry")
                    return_flag = False
            except:
                pass
        return return_flag

    # US20 Aunts and Uncles

    def AuntsAndUncles(self, indList, famList):
        return_flag = True
        util = gedUtil()
        TempNoneIndi = individual("temp")
        for family in famList:

            # Get the couple's IDs
            husband = TempNoneIndi
            wife = TempNoneIndi
            for ind in indList:
                if ind.indi == family.husband:
                    husband = ind
                if ind.indi == family.wife:
                    wife = ind
                if husband is not TempNoneIndi and wife is not TempNoneIndi:
                    break

            # Get the parents' IDs
            husband_mother = TempNoneIndi
            husband_father = TempNoneIndi
            wife_mother = TempNoneIndi
            wife_father = TempNoneIndi
            for child_fam in famList:
                # tu fix
                if husband.indi in child_fam.children:
                    husband_mother = child_fam.wife
                    husband_father = child_fam.husband
                if wife.indi in child_fam.children:
                    wife_mother = child_fam.wife
                    wife_father = child_fam.husband
                if husband_mother is not TempNoneIndi and wife_mother is not TempNoneIndi:
                    break
            try:
                # Wife is a sister to one of the husband's parents
                if husband_mother.familyC == wife.familyC or husband_father == wife.familyC:
                    print(
                        family.famid + "- Aunts and uncles should not marry their nieces or nephews")
                    return_flag = False

                # Husband is a brother to one of the wife's parents
                if wife_mother.familyC == husband.familyC or wife_father == husband.familyC:
                    print(
                        family.famid + "- Aunts and uncles should not marry their nieces or nephews")
                    return_flag = False
            except:
                pass
        return return_flag
# /Na
# Rh
    # US21 Correct gender for role

    def correctGender(self, indList, famList):
        outputindList = copy.deepcopy(indList)
        for ind in outputindList:
            if ind.husbID != "not mentioned":
                if ind.sex == "F":
                    ind.sex = "M"
                    print(ind.indi + " - GenderCorrect")
            elif ind.wifeID != "not mentioned":
                if ind.sex == "M":
                    ind.sex = "F"
                    print(ind.indi + " - GenderCorrect")
        return outputindList

    # US22 Unique IDs
    def noUnique_IDs(self, indList):
        nouniquelist = []
        Idlist = []
        for ind in indList:
            Idlist.append(ind.indi)
        checklist = set(Idlist)
        for id_check in checklist:
            count = 0
            for id_checks in Idlist:
                if id_check == id_checks:
                    count += 1
            if count > 1:
                nouniquelist.append(id_check)
        indList = gedHelper().MultipleidsDelete(nouniquelist, indList)
        return indList

    def noUnique_famIDs(self, famList):
        nouniquelist = []
        Idlist = []
        for fam in famList:
            Idlist.append(fam.famid)
        checklist = set(Idlist)
        for id_check in checklist:
            count = 0
            for id_checks in Idlist:
                if id_check == id_checks:
                    count += 1
            if count > 1:
                nouniquelist.append(id_check)
        famList = gedHelper().MultipleidsDelete2(nouniquelist, famList)
        return famList

    def MultipleidsDelete(self, nouniquelist, indList):
        for id_checks in nouniquelist:
            count = 1
            for ind in indList:
                if ind.indi == id_checks:
                    count += 1
                if count > 2:
                    if ind in indList:
                        indList.remove(ind)
                        print(ind.indi + " - noUnique_IDs")
        return indList

    def MultipleidsDelete2(self, nouniquelist, famList):
        for id_checks in nouniquelist:
            count = 1
            for fam in famList:
                if fam.famid == id_checks:
                    count += 1
                if count > 2:
                    if fam in famList:
                        famList.remove(fam)
        return famList

# /Rh
# Kt
    # US23 Unique name and birth date
    # I overide the __hash__ and __eq__ to implement this.
    def UniqueNameAndBirth(self, indList):
        re = set(indList)
        if len(re) != len(indList):
            print("Exist Duplicated Data")
        return re

    # US24 Unique families by spouses
    def UniqueFamily(self, famList):
        re = set(famList)
        if len(re) != len(famList):
            print("Exist Duplicated Data")
        return re
# /Kt
# Sb
    # US25 Unique child names in families

    def UniqueChildName(self, famList, indList):
        util = gedUtil()
        outputindList = copy.deepcopy(famList)
        for family in famList:
            childName = []

            for child in family.children:
                for ind in indList:
                    if ind.indi == family.children:
                        child == ind
                        childName.append(child.name)

            if(len(childName) != (len(set(childName)))):
                outputindList.remove(family)
                break
        return outputindList
    
    #US26 List all births in the GedCom file    
    def listBirths(self,indList):
        birth = []
        for ind in indList:
            if ind.birth != "not mentioned":
                birth.append(ind)
        return birth
# /Sb
# Cs
    # US27 Include person's current age when listing individuals.

    def LoadAgeForPerson(self, person):
        return gedUtil().getAge(person)

    # US28 Order siblings by age
    def orderSibling(self, indList, fam):
        util = gedUtil()
        siblings = []
        children = []
        ordered = []
        for child in fam.children:
            children.append(str(child))
        for ind in indList:
            indi = str(ind.indi)
            for child in children:
                if (indi == child):
                    siblings.append(ind)
        while len(siblings) > 0:
            oldest = siblings[0]
            for sibling in siblings:
                if util.getAge(sibling) > util.getAge(oldest):
                    oldest = sibling
            ordered.append(siblings.pop(siblings.index(oldest)))
        return ordered
# /Cs
# Na
    # US29 List Deceased

    def listDeceased(self, indList):
        deceased = []
        for ind in indList:
            if ind.death != "not mentioned":
                deceased.append(ind)
                print(ind.indi + " - Deceased")
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
                print(husband_id + " and " + wife_id + " - Married")
        return living
# /Na
#Rh
    #US31 List living single
    def livingsingle(self, indList, famList):
        living =[]
        livingsingle =[]
        for ind in indList:
            if ind.death != "not mentioned":
                living.append(ind)
        for ind in living:
            if ind.marDate =="not mentioned":
                if gedUtil().getAge(ind.birth) >30:
                    livingsingle.append(ind.name)
                    print(ind.name+ "is living")
        return livingsingle

    #US32 List multiple births
    def multiplebirths(self, indList, famList):
        singlebirth = []
        multiplebirth = []
        count = 0
        for ind in indList:
            singlebirth.append(ind.birth)
        set(singlebirth)
        for single in singlebirth:
            for ind in indList:
                if ind.birth == single:
                    count +=1
                if count > 1:
                    multiplebirth.append(ind.name)
        return multiplebirth      
#/Rh
#Kt
    #US33 List orphans
    def listOrphans(self, indList):
        childPrefix = []
        orphanList = []
        for person in indList:
            if (person.age != 'ERROR: INVALID DATE') :
                if int(person.age) < 18:
                    childPrefix.append(person)
        for child in childPrefix:
            if child.family == "not mentioned":
                orphanList.append(child)
                print(child.name +" - is orphan")
        return orphanList
    
    #US34 List large age differences
    def listLargeAgeDifference(self, indList,famList):
        re = []
        for f in famList:
            husAge = gedHelper().getIndi(indList,f.husband).age
            wifAge = gedHelper().getIndi(indList,f.wife).age

            if  husAge != -1 and wifAge != -1:
                if (husAge>wifAge):
                    if (husAge>= wifAge*2):
                        re.append(f)
                        print(f.famid  +" - is a large age difference family")
                else:
                    if (wifAge>= husAge*2):
                        re.append(f)
                        print(f.famid  +" - is a large age difference family")
        return re
    
    def getIndi(self,indList, indiStr):
        for i in indList:
            if i.indi == indiStr:
                return i
        return individual("empty",age=-1)
#/Kt
#Sb
 #US35 List recent birthdays
    def recentBirthdays(self, indList):
        birthdays = []
        for ind in indList:
            if ind.birth != "not mentioned":
                if gedUtil().dateLessThanThirtyDays(ind.birth): 
                    birthdays.append(ind)
        if len(birthdays) > 0:
            for ind in birthdays:
                print(ind.name+ "- Recent Birth")
        return

#US36 List recent deaths	
    def recentDeaths(self, indList):
        death = []
        for ind in indList:
            if gedUtil().dateLessThanThirtyDays(ind.death):
                death.append(ind)
        if len(death) > 0:
            for ind in death:
                print(ind.name + "- Recent Death")
        return
#/Sb
#Cs
    #US37 List recent survivors
    def recentSurvivors(self, indList, famList):
        for ind in indList:
            if ind.death != "not mentioned":
                if gedUtil().dateLessThanThirtyDays(ind.death):
                    print("Recently deceased: " + ind.name)
                    if ind.husbID != "not mentioned":
                        for h in indList:
                            if h.indi == ind.husbID:
                                if h.death == "not mentioned":
                                    print("Surviving husband: " + h.name)
                                    break
                    if ind.wifeID != "not mentioned":
                        for w in indList:
                            if w.indi == ind.wifeID:
                                if w.death == "not mentioned":
                                    print("Surviving wife: " + w.name)
                                    break
                    for fam in famList:
                        if fam.famid == ind.family:
                            if len(fam.children) > 0:
                                print("-Surviving Descendants-")
                                print(*fam.children, sep = ", ")
        return

    #US38 List upcoming birthdays
    def upcomingBirthdays(self, indList):
        birthdays = []
        for ind in indList:
            if ind.death == "not mentioned" and gedUtil().dateWithin30Days(ind):
                birthdays.append(ind)
        if len(birthdays) > 0:
            for ind in birthdays:
                print(ind.name)
        return birthdays
#/Cs
#Na
    # US39 List Upcoming Anniversaries
    def Anniversary(self, famList):
        anniversaries = []
        # Get the current day and month. Year does not matter
        #fixed by tu
        currentMonth = datetime.datetime.now().month
        currentDay = datetime.datetime.now().day
        for fam in famList:
            # Check if the family is married and not divorced
            if fam.marDate is not "not mentioned" and fam.divDate is "not mentioned":
                marriage = gedUtil().getDate(fam.marDate)
                # If the month is later than the current, append it
                if marriage.month > currentMonth:
                    anniversaries.append(marriage)
                # If the month is the current and the day is later, append it
                if marriage.month == currentMonth and marriage.day > currentDay:
                    anniversaries.append(marriage)
        for ann in anniversaries:
            print(ann)

    #US 40 is in Util

#/Na