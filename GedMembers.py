
__author__= 'tutu'

Valid = {'INDI': 0, 'NAME': 1, 'SEX': 1, 'BIRT': 1, 'DEAT': 1, 'FAMC': 1, 'FAMS': 1, 'FAM': 0,
         'MARR': 1, 'HUSB': 1, 'WIFE': 1, 'CHIL': 1, 'DIV': 1, 'DATE': 2, 'HEAD': 0, 'TRLR': 0, 'NOTE': 0}

class individual(object):


    #Add the property you need here
    def __init__(
        self,
        indi,
        name= "empty",
        sex = "not mentioned",
        birth ="not mentioned",
        death ="not mentioned",
        marrigeDate = "not mentioned",
        divorceDate = "not mentioned",
        family ="not mentioned",
        husbID ="not mentioned",
        wifeID ="not mentioned",
        children = "not mentioned"):
        self.indi = indi
        self.name = name
        self.sex = sex
        self.birth = birth
        self.death = death
        self.marDate = marrigeDate
        self.divDate = divorceDate
        self.family = family
        self.husbID = husbID
        self.wifeID = wifeID
        self.children = children


    def printBriefInfo(self):
        print("ID:"+self.indi+" Name:"+self.name)

    def printInfo(self):
        print("=====================")
        print("ID:      " + self.indi)
        print("Name:    " + self.name)
        print("Sex:     " + self.sex)
        print("Birth:   " + self.birth)
        print("Death:   " + self.death)
        print("MarrigeDate:   " + self.marDate)
        print("DivorceDate:   " + self.divDate)
        print("Family:  " + self.family)
        print("HusbID:  " + self.husbID)
        print("WifeID:  " + self.wifeID)
        print("Children:" + self.children)
        print("=====================")

class family(object):

    def __init__(
        self,
        famid,
        familyNickname ="not mentioned",
        husband ="not mentioned",
        wife ="not mentioned",
        children = "not mentioned"):
        self.famid = famid
        self.husband = husband
        self.wife = wife

    def printBriefInfo(self):
        print("FamilyID: " + self.famid + " HusbID:" +self.husband +" WifeID:" +self.wife)