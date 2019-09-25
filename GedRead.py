#!/usr/bin/python
# -*- coding: UTF-8 -*-

Valid = {'INDI': 0, 'NAME': 1, 'SEX': 1, 'BIRT': 1, 'DEAT': 1, 'FAMC': 1, 'FAMS': 1, 'FAM': 0,
         'MARR': 1, 'HUSB': 1, 'WIFE': 1, 'CHIL': 1, 'DIV': 1, 'DATE': 2, 'HEAD': 0, 'TRLR': 0, 'NOTE': 0}

indList = []


def isValid(level, tag):
    if tag in Valid:
        if level == str(Valid[tag]):
            return "Y"
        else:
            return "N"
    else:
        return "N"

def individuals(line):
    if line[3] == 'INDI':
        inside = False
        for x in indList:
            if line[1] is x:
                inside = True
            if inside is False:
                indList.append(line[1])
    if line[1] == 'NAME':
        inside = False
        for x in indList:
            if line[3] is x:
                inside = True
            if inside is False:
                indList.append(line[3])


def readGed(file):
    try:
        myGed = open(file, "r")
        gedLines = myGed.readlines()
        for line in gedLines:
            # 把换行符给删喽,再加个尾空格方便索引处理
            line = line[:-1]
            line = line + " "
            # 读取每行的数据并用切片存入list
            linedata = [line[0:1], line[2:line.index(" ", 2)], "Valid", line[line.index(" ", 2) + 1:-1]]
            linedata[2] = isValid(linedata[0], linedata[1])
            individuals(linedata)
            # 输出
            print("-->" + line[:-1])
            print("<--" + linedata[0] + "|" + linedata[1] + "|" + linedata[2] + "|" + linedata[3])
        print(*indList, sep = '\n')
    finally:
        myGed.close()


if __name__ == '__main__':
    readGed("Group 5 GED.ged")
