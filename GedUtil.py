import datetime
from datetime import date
from datetime import timedelta

class gedUtil(object):

    def __init__(self):
        pass
    
    def getAge(self,person):
        try:
            temp = person.birth
            if (temp != "not mentioned"):
                birthYear = datetime.datetime.strptime(temp,'%d %b %Y').year
                currentYear = datetime.datetime.now().year
                return currentYear-birthYear
            else:
                return None
        except:
            print("Wrong Input")
    
    #Used for U37
    def dateLessThanThirtyDays(self,date1):
        try:
            a = datetime.datetime.strptime(date1,'%d %m %Y')
            b = datetime.datetime.now()
            c = b - a
            return c.days <= 30
        except:
            print("Wrong Input")

    #Used for U38
    def dateWithin30Days(self,ind):
        try:
            birthMonth = datetime.datetime.strptime(ind.birth,'%d %m %Y').month
            birthDay = datetime.datetime.strptime(ind.birth,'%d %m %Y').day
            birth = 0 + timedelta(birthMonth) + timedelta(birthDay)
            checkMonth = datetime.datetime.now().month
            checkDay = datetime.datetime.now().day
            check = 0 + timedelta(checkMonth) + timedelta(checkDay)
            result = check - birth
            return result.days <= 30 and result.days > 0
        except:
            print("Wrong Input")

    def dateCompare(self,dateA,dateB):
        try:
            a = datetime.datetime.strptime(dateA,'%d %b %Y')
            b = datetime.datetime.strptime(dateB,'%d %b %Y')
            return a.__gt__(b)
        except:
            print("Wrong Input")

    def getDate(self,dateStr):
        if (dateStr != "not mentioned") and (dateStr is not None):
            return datetime.datetime.strptime(dateStr,'%d %b %Y')
        else:
            return None

    def getBirthStrByIndi(self,indi,indList):
        re = "not mentioned"
        for person in indList:
            if person.indi == indi:
                re = person.birth
                break
        return re

    
