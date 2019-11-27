#!/usr/bin/python
# -*- coding: UTF-8 -*-

# @author Tu Kechao

from GedMembers import Valid
from GedMembers import individual
from GedMembers import family
from GedHelper import gedHelper
from GedUtil import gedUtil
from prettytable import PrettyTable

import datetime
import traceback
import copy
import sys

indList = []
famList = []
linedataList = []

errorList = []

indLength = 5000
famLength = 1000


# To get data in lines and store in a list
def infoProcess(line: "Data line", type: "1 for indi 2 for fam"):
    ListTemp = copy.deepcopy(linedataList[0: -1])
    BlockList = []
    if type == 1:
        Cond = 'INDI'
    elif type == 2:
        Cond = 'FAM'
    else:
        RuntimeError
    Count = 0
    # Label the individual
    for i in enumerate(ListTemp):
        if ListTemp[i[0]][3] == Cond:
            Count += 1
        ListTemp[i[0]].insert(0, Count)
    # Save the Info Block
    for j in range(1, Count+1):
        tempBlock = []
        for item in ListTemp:
            if item[0] is j:
                tempBlock.append(item)
            if item[0] is j+1:
                break
        BlockList.append(tempBlock)
    # Get the Info From Block
    if type == 1:
        getIndInfoFromBlocks(BlockList)
    elif type == 2:
        getFamInfoFromBlocks(BlockList)


def isValid(level: "tag level", tag: "tag name") -> str:
    if tag in Valid:
        if level == str(Valid[tag]):
            return "Y"
        else:
            return "N"
    else:
        return "N"


def getNameByIndi(indi):
    re = "Not Mentioned"
    for person in indList:
        if person.indi == indi:
            re = person.name
            break
    return re


def readGed(file):
    try:
        validity = 'valid'
        myGed = open(file, "r")
        gedLines = myGed.readlines()
        gedLines.append("END END END")
        for line in gedLines:
            # Do line cut and store the whole line
            line = line + " "
            linedata = [line[0:1], line[2:line.index(
                " ", 2)], "Valid", line[line.index(" ", 2) + 1:-1]]
            linedata[2] = isValid(linedata[0], linedata[1])
            linedata[3] = linedata[3].replace("\n", "")
            linedataList.append(linedata)

        infoProcess(linedataList, 1)
        infoProcess(linedataList, 2)
        myGed.close()
    except:
        print("Invalid file")
        validity = 'invalid'
        myGed.close()
    finally:
        return validity


def getIndInfoFromBlocks(blocks):
    for infoBlock in blocks:
        if len(indList) < indLength:
            tempIndi = individual(None)
            for index, infoLine in enumerate(infoBlock):
                # deal with properties here
                if infoLine[4] == 'INDI':
                    tempIndi.indi = infoLine[2]  # Kt
                if infoLine[2] == 'SEX':
                    tempIndi.sex = infoLine[4]  # Kt
                if infoLine[2] == 'NAME':
                    tempIndi.name = infoLine[4]  # Kt
                if infoLine[2] == 'BIRT\n':
                    tempIndi.birth = datetime.datetime.strftime(
                        gedUtil().getDate(infoBlock[index+1][4]), '%d %b %Y')  # Kt
                if infoLine[2] == 'DEAT':
                    tempIndi.death = datetime.datetime.strftime(
                        gedUtil().getDate(infoBlock[index+1][4]), '%d %b %Y')  # Kt
                if infoLine[2] == 'FAMC':
                    tempIndi.familyC = infoLine[4]  # Na
                # if infoLine[2] == 'FAMS':
                   # tempIndi.familyS.append(infoLine[4])
            indList.append(tempIndi)
        else:
            print("Maximum amount of individuals stored!\n")


def getFamInfoFromBlocks(blocks):
    for infoBlock in blocks:
        if len(famList) < famLength:
            tempFam = family(None)
            for index, infoLine in enumerate(infoBlock):
                if infoLine[4] == 'FAM':
                    tempFam.famid = infoLine[2]
                if infoLine[2] == 'HUSB':
                    tempFam.husband = infoLine[4]
                if infoLine[2] == 'WIFE':
                    tempFam.wife = infoLine[4]
                if infoLine[2] == 'CHIL':
                    tempFam.children.append(infoLine[4])
                if infoLine[2] == 'MARR\n':
                    tempFam.marDate = datetime.datetime.strftime(
                        gedUtil().getDate(infoBlock[index+1][4]), '%d %b %Y')
                if infoLine[2] == '_SEPR\n':
                    tempFam.divDate = datetime.datetime.strftime(
                        gedUtil().getDate(infoBlock[index+1][4]), '%d %b %Y')
            famList.append(tempFam)
        else:
            print("Maximum amount of families stored!\n")
    # Search the name for them and add
    for fam in famList:
        for person in indList:
            if person.indi == fam.husband:
                fam.husbandN = person.name
                person.marDate = fam.marDate
                person.divDate = fam.divDate
                person.wifeID = fam.wife
            if person.indi == fam.wife:
                fam.wifeN = person.name
                person.marDate = fam.marDate
                person.divDate = fam.divDate
                person.husbID = fam.husband


# In this method we process individuals List with all those US
# Cuz some data will add to individual after reading the family infos
# We have to do data processing in seperate.
def gedHelperIndProcess() -> list:
    try:
        gh = gedHelper()
        outputindList = copy.deepcopy(indList)
        #US12
        errorList.append(gh.validParentsage(indList,famList))
        

        for i in indList:
            if gh.datebeforeCurrentdate(i) == False:
                Log = "datebeforeCurrentdate - " + i.indi
                errorList.append(Log)
                continue
            if gh.birthBeforeMarriage(i) == False:
                Log = "birthBeforeMarriage - " + i.indi
                errorList.append(Log)
                continue  # if current item deleted,we dont need to go further
            if gh.birthBeforeDeath(i) == False:
                Log = "birthBeforeDeath - " + i.indi
                errorList.append(Log)
                continue
            if gh.marriageBeforeDivorce(i) == False:
                Log = "marriageBeforeDivorce - " + i.indi
                errorList.append(Log)
                continue
            if gh.marriageBeforeDeath(i) == False:
                Log = "marriageBeforeDeath - " + i.indi
                errorList.append(Log)
                continue
            if gh.divorceBeforeDeath(i) == False:
                Log = "divorceBeforeDeath - " + i.indi
                errorList.append(Log)
                continue

            # if gh.lessThan150Years(i) == False:
            #   errorList.append(Log)

        #US11
        return outputindList
    except Exception:
        print("Bug")
        print(traceback.format_exc())


def gedHelperFamProcess() -> list:
    gh = gedHelper()
    outputfamList = copy.deepcopy(famList)
    outputfamList = gh.nobigamy(indList,famList)
    outputfamList = gh.MultipleBirthsDelete(indList,famList)
    outputfamList = gh.SiblingsSpacing(indList,famList)
    gh.marriageToDescendant(indList,famList)
    gh.siblingsMarried(indList,famList)
    gh.AuntsAndUncles(indList,famList)

    return outputfamList


def GedReader(file):
    readGed(file)
    # gedHelper().validate_family(indList,famList)
    outputindList = copy.deepcopy(indList)
    outputfamList = copy.deepcopy(famList)

    print("=====Origin Individual List Table=====")
    indiTable = PrettyTable(["indi",
                             "name",
                             "sex",
                             "birth",
                             "death",
                             # "marrigeDate",
                             # "divorceDate",
                             "family",
                             "husbID",
                             "wifeID",
                             # "familyC",
                             # "age",
                             # "orphan"
                             ])

    if outputindList is not None:
        for person in outputindList:
            indiTable.add_row([person.indi,
                               person.name,
                               person.sex,
                               person.birth,
                               person.death,
                               # person.marDate,
                               # person.divDate,
                               person.family,
                               person.husbID,
                               person.wifeID,
                               # person.familyC,
                               # person.age,
                               # person.orphan
                               ])

        print(indiTable)

    print("=====Origin Family List Table=====")
    if outputindList is not None:
        famTable = PrettyTable([
            "famid",
            "husband",
            "wife",
            "marDate",
            "divDate"
        ])
        for family in outputfamList:
            famTable.add_row([
                family.famid,
                family.husband,
                family.wife,
                family.marDate,
                family.divDate
            ])
        print(famTable)
    print("=====Error List=====")

    gedHelper().validBirth(indList, famList)
    gedHelper().validMarriage(indList, famList)
    outputindList = gedHelperIndProcess()
    outputfamList = gedHelperFamProcess()
    for error in errorList:
        print(error)
    

    


if __name__ == '__main__':
    GedReader(".\\TestGed\\Group 5 GED.ged")
