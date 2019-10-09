
Valid = {'INDI': 0, 'NAME': 1, 'SEX': 1, 'BIRT': 1, 'DEAT': 1, 'FAMC': 1, 'FAMS': 1, 'FAM': 0,
         'MARR': 1, 'HUSB': 1, 'WIFE': 1, 'CHIL': 1, 'DIV': 1, 'DATE': 2, 'HEAD': 0, 'TRLR': 0, 'NOTE': 0}

class individual(object):

    def __init__(self, indi, *args):
        self.indi = indi
        self.name = args[0]

    def printInfo(self):
        print("ID is: " + self.indi)
        print("Name is: " + self.name)

class family(object):

    def __init__(self, famid,*args):
        self.famid = famid
        while len(args)<4:
            args = args+(None,)

        self.husband = args[0]
        self.wife = args[1]
        self.husbandN = args[2]
        self.wifeN = args[3]

    def printInfo(self):
        print("Family ID is: " + self.famid)
        if self.husband != None:
            print("Husband is: " + self.husbandN)
        if self.wife != None:
            print("Wife is: " + self.wifeN)