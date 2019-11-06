import datetime

temp ='14 SEP 1996'

birthYear = datetime.datetime.strptime(temp,'%d %b %Y').year
currentYear = datetime.datetime.now().year


print(currentYear-birthYear)