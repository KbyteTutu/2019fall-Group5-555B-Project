import datetime
from datetime import date
from datetime import timedelta

class gedUtil(object):

    def __init__(self):
        pass
    

    def InvalidDate(self):
        error = "ERROR: INVALID DATE"
        return error

    def getAge(self,person):
        try:
            temp = person.birth
            if (temp != "not mentioned"):
                try:
                    birthYear = datetime.datetime.strptime(temp,'%d %b %Y').year
                    currentYear = datetime.datetime.now().year
                    return currentYear-birthYear
                except:
                    return gedUtil().InvalidDate()
            else:
                return None
        except:
            print("Wrong Input Age")
    


    def dateCompare(self,dateA,dateB):
        try:
            a = datetime.datetime.strptime(dateA,'%d %b %Y')
            b = datetime.datetime.strptime(dateB,'%d %b %Y')
            return a.__gt__(b)
        except:
            print("Wrong Input dateCompare")

    # US40 Reject Illegitimate Dates
    def getDate(self,dateStr):
        if (dateStr != "not mentioned") and (dateStr is not None):
            # If it cannot be converted to a datetime object, then it is an invalid date
            try:
                return datetime.datetime.strptime(dateStr,'%d %b %Y')
            except:
                return gedUtil().InvalidDate()
        else:
            return None

    def getBirthStrByIndi(self,indi,indList):
        re = "not mentioned"
        for person in indList:
            if person.indi == indi:
                re = person.birth
                break
        return re
    
