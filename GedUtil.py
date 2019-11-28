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
        except Exception as e:
            print("Wrong Input Age")
    
#Used for U37
    def dateLessThanThirtyDays(self,date1):
        if date1 != 'not mentioned':
            try:
                a = datetime.datetime.strptime(date1,'%d %b %Y')
                b = datetime.datetime.now()
                c = b - a
                return c.days <= 30
            except Exception as e:
                print(str(e))
        else:
            return False

    #Used for U38
    def dateWithin30Days(self,ind):
        try:
            birthMonth = datetime.datetime.strptime(ind.birth,'%d %b %Y').month
            birthDay = datetime.datetime.strptime(ind.birth,'%d %b %Y').day
            birth = timedelta(birthMonth) + timedelta(birthDay)
            checkMonth = datetime.datetime.now().month
            checkDay = datetime.datetime.now().day
            check = timedelta(checkMonth) + timedelta(checkDay)
            result = check - birth
            return result.days <= 30 and result.days > 0
        except Exception as e :
            print(str(e))

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
    
