#!/usr/bin/python
# -*- coding: UTF-8 -*-

from GedMembers import Valid
from GedMembers import individual
from GedMembers import family
from GedHelper import gedHelper


import copy
import sys

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





def isValid(level:"tag level", tag:"tag name") -> str:
    if tag in Valid:
        if level == str(Valid[tag]):
            return "Y"
        else:
            return "N"
    else:
        return "N"

def getNameByIndi(indi):
    re = "Invalid / Not Mentioned"
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
            #Do line cut and store the whole line
            line = line + " "
            linedata = [line[0:1], line[2:line.index(" ", 2)], "Valid", line[line.index(" ", 2) + 1:-1]]
            linedata[2] = isValid(linedata[0], linedata[1])
            linedata[3] = linedata[3].replace("\n","")
            linedataList.append(linedata)

        infoProcess(linedataList,1)
        infoProcess(linedataList,2)
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
            for index in range(len(infoBlock)):
                # deal with properties here
                if infoBlock[index][4] == 'INDI':
                    tempIndi.indi = infoBlock[index][2]#Kt
                if infoBlock[index][2] == 'NAME':
                    tempIndi.name = infoBlock[index][4]#Kt
                if infoBlock[index][2] == 'BIRT\n':
                    tempIndi.birth = infoBlock[index+1][4]#Kt
                if infoBlock[index][2] == 'DEAT':
                    tempIndi.death = infoBlock[index+1][4]#Kt
                # Marriage/Divorce date is about to add
                if infoBlock[index][2] == 'FAMC':
                    tempIndi.familyC = infoBlock[index][4]#Na
                #if j[2] == 'FAMS':
                #    tempIndi.familyS.append(j[4])
            indList.append(tempIndi)
        else:
            print("Maximum amount of individuals stored!\n")

def getFamInfoFromBlocks(blocks):
    for infoBlock in blocks:
        if len(famList) < famLength:
            tempFam = family(None)
            for infoLine in infoBlock:
                if infoLine[4] == 'FAM':
                    tempFam.famid = infoLine[2]
                if infoLine[2] == 'HUSB':
                    tempFam.husband = infoLine[4]
                if infoLine[2] == 'WIFE':
                    tempFam.wife = infoLine[4]
            famList.append(tempFam)
        else:
            print("Maximum amount of families stored!\n")
    #Search the name for them and add
    #Read Family data and add it to individual
    for spouse in famList:
        for person in indList:
            if  person.indi == spouse.husband:
                spouse.husbandN = person.name
            if  person.indi == spouse.wife:
                spouse.wifeN = person.name


def GedReader(file):
    if readGed(file):
        gh = gedHelper()
        #put all our user story here.
        gh.validate_family(indList,famList)
        gh.validBirth(indList,famList)
        gh.validMarriage(indList,famList)

        for i in indList:
            #if gh.datebeforeCurrentdate(i) == False:
            #    inList.remove(i)
            #if gh.birthBeforeMarriage(i) == False:
            #    inList.remove(i)
            if gh.birthBeforeDeath(i) == False:
                indList.remove(i)
            #if gh.marriageBeforeDivorce(i) == False:
            #    indList.remove(i)
            #if gh.lessThan150Years(i) == False:
            #    indList.remove(i)


        print("=====Individuals=====")
        for i in indList:
            i.printBriefInfo()
        print("=====Family=====")
        for j in famList:
            print("FamilyID:"+j.famid+ " Husband Name:"+ getNameByIndi(j.husband) + " Wife Name:" + getNameByIndi(j.wife))


if __name__ == '__main__':
    GedReader(".\\TestGed\\Group 5 GED.ged")
