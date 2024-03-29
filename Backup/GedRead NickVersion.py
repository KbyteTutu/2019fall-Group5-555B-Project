﻿#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

indList = []
indLength = 0

def isValid(level, tag):
    if tag in Valid:
        if level == str(Valid[tag]):
            return "Y"
        else:
            return "N"
    else:
        return "N"

def individuals(line):
    if indLength <= 5000:
        if line[3] == 'INDI':
            inside = False
            while not inside:
                if line[1] in indList:
                    inside = True
                if inside is False:
                    indList.append(line[1])
        if line[1] == 'NAME':
            inside = False
            while not inside:
                if line[3] in indList:
                    inside = True
                    # Remove the ID from the list if the name is not being added
                    indList.pop()
                if inside is False:
                    indList.append(line[3])
                    # Increase counter after successful insert of an ID and Name
                    indLength = ++indLength
    else:
        print("Maximum amount of individuals stored!\n")
   

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
        #print(*indList, sep = '\n')
        while i < indLength:
            # Print layout: "ID Name"
            print(indList[i] + " " + indList[i+1] + "\n")
            i = i + 2
    finally:
        myGed.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 
        # Usage python GedRead.py firstfile
        sys.exit(1)
    readGed(sys.argv[1])
