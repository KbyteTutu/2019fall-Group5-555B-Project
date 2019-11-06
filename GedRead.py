#!/usr/bin/python
# -*- coding: UTF-8 -*-

from GedMembers import Valid
from GedMembers import individual
from GedMembers import family
import copy
import sys
import datetime

indList = []
famList = []
linedataList = []

indLength = 5000
famLength = 1000

def infoProcess(line:"Data line",type:"1 for indi 2 for fam"):# To get data in lines and store in a list
    ListTemp = copy.deepcopy(linedataList[0: -1])
    BlockList = []
    if type == 1:
        Cond = 'INDI'
    elif type == 2:
        Cond = 'FAM'
    else:
        RuntimeError
    Count= 0
    # Label the individual
    for i in enumerate(ListTemp):
        if ListTemp[i[0]][3] == Cond:
            Count += 1
        ListTemp[i[0]].insert(0,Count)
    # Save the Info Block
    for j in range(1,Count):
        tempBlock = []
        for item in ListTemp:
            if item[0] is j:
                tempBlock.append(item)
            if item[0] is j+1:
                break
        BlockList.append(tempBlock)
    # Get the Info From Block
    if type==1:
        getIndInfoFromBlocks(BlockList)
    elif type ==2:
        getFamInfoFromBlocks(BlockList)

def getIndInfoFromBlocks(blocks):
    date_type = None
    for i in blocks:
        if len(indList) < indLength:
            tempIndi = individual(None,None)
            for j in i:     
                if j[4] == 'INDI':
                    tempIndi.indi = j[2]
                if j[2] == 'NAME':
                    tempIndi.name = j[4]
                if j[2] == 'SEX':
                    tempIndi.sex = j[4]
                if j[2] == 'BIRT':
                    date_type = 'BIRT'
                if j[2] == 'DEAT':
                    date_type = 'DEAT'
                if j[2] == 'DATE':
                    if date_type == "BIRT":
                        tempIndi.birth = j[4]
                        date_type = None
                    elif date_type == "DEAT":
                        tempIndi.death = j[4]
                        date_type = None
                    else:
                        print("ERROR: Invalid Date in Ged")
                if j[2] == 'FAMC':
                    tempIndi.familyC = j[4]
                #if j[2] == 'FAMS':
                #    tempIndi.familyS.append(j[4])
            indList.append(tempIndi)
        else:
            print("Maximum amount of individuals stored!\n")

def getFamInfoFromBlocks(blocks):
    for i in blocks:
        if len(famList) < famLength:
            tempFam = family(None,None)
            for j in i:
                if j[4] == 'FAM':
                    tempFam.famid = j[2]
                if j[2] == 'HUSB':
                    tempFam.husband = j[4]
                if j[2] == 'WIFE':
                    tempFam.wife = j[4]
            famList.append(tempFam)
        else:
            print("Maximum amount of families stored!\n")
    #Search the name for them and add
    for spouse in famList:
        for person in indList:
            if  person.indi == spouse.husband:
                spouse.husbandN = person.name
            if  person.indi == spouse.wife:
                spouse.wifeN = person.name



def isValid(level:"tag level", tag:"tag name") -> str:
    if tag in Valid:
        if level == str(Valid[tag]):
            return "Y"
        else:
            return "N"
    else:
        return "N"

def validate_family(indList,famList):
    for family in famList:
        for ind in indList:
            if(ind.familyC== family.famid):
                if ind.sex != 'M' and ind.sex != 'F':
                    return False
        if family.husband != "invalid/not mentioned" and family.husband.sex != 'M':
            return False
        if family.wife != "invalid/not mentioned" and family.wife.sex != 'F':
            return False


def getNameByIndi(indi):
    re = "Invalid / Not Mentioned"
    for person in indList:
        if person.indi == indi:
            re = person.name
            break
    return re

def getDate(date):
    string = date
    string = string.split(whiteSpaceRegex);
    date = datetime(
        int(string[2]),
        datetime.strptime(string[1], '%b').month,
        int(string[0]))
    return date

def validBirth(indList, famList):
    return_flag = True
    for ind in indList:
        if ind.familyC != "not mentioned":
            father = None
            fatherID = None
            mother = None
            montherID = None
            fam = None

            for family in famList:
                if family.famid == ind.familyC:
                    fatherID = family.husband
                    motherID = family.wife
                    fam = family
                    break

            for inds in indList:
                if inds.indi == fatherID:
                    father = inds
                if inds.indi == motherID:
                    mother = inds

            if getDate(father.death) is not None and getDate(father.death) < getDate(ind.birth) - timedelta(days=266):
                print("Child is born more than 9 months after death of father")
                return_flag = False
            if getDate(mother.death) is not None and getDate(mother.Death) < getDate(ind.birth):
                print("Child is born after death of mother")
                return_flag = False
    return return_flag

def validMarriage(indList, famList):
    return_flag = True
    current = datetime.today()
    min_birth = datetime(current.year - 14, current.month, current.day)

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

        if getDate(husband.birth) > min_birth:
            print(husband + " is married before 14 years old")
            return_flag = False
        
        if getDate(wife.birth) > min_birth:
            print(wife + " is married before 14 years old")
            return_flag = False

        return return_flag



def readGed(file):
    #indList = []
    #famList = []
    #linedataList = []

    #indLength = 5000
    #famLength = 1000
    validity = 'valid'
    validate_family(indList,famList)
    
    try:
        myGed = open(file, "r")
        gedLines = myGed.readlines()
        gedLines.append("END END END")
        for line in gedLines:
            #Do line cut and store the whole line
            line = line + " "
            linedata = [line[0:1], line[2:line.index(" ", 2)], "Valid", line[line.index(" ", 2) + 1:-1]]
            linedata[2] = isValid(linedata[0], linedata[1])
            linedata[3] = linedata[3].replace("\n","")
            linedataList.append(linedata)

        infoProcess(linedataList,1)
        infoProcess(linedataList,2)
        print("=====Individuals=====")
        for i in indList:
            i.printBriefInfo()
            i.printInfo()
        print("=====Family=====")
        for j in famList:
            print("FamilyID:"+j.famid+ " Husband Name:"+ getNameByIndi(j.husband) + " Wife Name:" + getNameByIndi(j.wife))

        myGed.close()
    except:
        print("Invalid file")
        validity = 'invalid'
        myGed.close()
    finally:
        return validity


def readGedTest(file, temp, ind):
    indList = []
    famList = []
    linedataList = []

    indLength = 5000
    famLength = 1000
    try:
        myGed = open(file, "r")
        gedLines = myGed.readlines()
        gedLines.append("END END END")
        for line in gedLines:
            #Do line cut and store the whole line
            line = line + " "
            linedata = [line[0:1], line[2:line.index(" ", 2)], "Valid", line[line.index(" ", 2) + 1:-1]]
            linedata[2] = isValid(linedata[0], linedata[1])
            linedata[3] = linedata[3].replace("\n","")
            linedataList.append(linedata)

        infoProcess(linedataList,1)
        infoProcess(linedataList,2)
        print("=====Individuals=====")
        for i in indList:
            i.printBriefInfo()
        print("=====Family=====")
        for j in famList:
            print("FamilyID:"+j.famid+ " Husband Name:"+ getNameByIndi(j.husband) + " Wife Name:" + getNameByIndi(j.wife))

        if ind == True:
            temp = indList
        if ind == False:
            temp = famList
        myGed.close()
    except:
        print("Invalid file")
        myGed.close()
    finally:
        return temp




if __name__ == '__main__':
    readGed("Group 5 GED.ged")
