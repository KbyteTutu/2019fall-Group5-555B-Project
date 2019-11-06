__author__= 'Group5'

from GedMembers import Valid
from GedMembers import individual
from GedMembers import family
from GedUtil import gedUtil

class gedHelper(object):

    def __init__(self):
        pass

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


