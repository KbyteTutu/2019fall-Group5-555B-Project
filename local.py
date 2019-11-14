import datetime


d1 = datetime.datetime.strptime("28 APR 1998",'%d %b %Y')
d2 = datetime.datetime.strptime("24 APR 1999",'%d %b %Y')

d = (d1 - d2)
d = abs(d)
if (d.days>2) and (d.days<240):
    print (d.days)
    print ("wrong")