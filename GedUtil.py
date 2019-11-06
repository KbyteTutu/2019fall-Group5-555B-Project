import datetime

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
                return 0
        except:
            print("Wrong Input")

    def dateCompare(self,dateA,dateB):
        try:
            a = datetime.datetime.strptime(dateA,'%d %b %Y')
            b = datetime.datetime.strptime(dateB,'%d %b %Y')
            return a.__gt__(b)
        except:
            print("Wrong Input")