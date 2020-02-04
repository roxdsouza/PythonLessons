import datetime

print '------------Date Time-----------------'

print str(datetime.datetime(1977, 12, 14, 17, 30))
print 'Today is :', datetime.datetime.today()

other = datetime.datetime(1977, 12, 14, 17, 30)
now = datetime.datetime.today()

print now - other
print other - now

mylist = []
mylist.append(datetime.date.today())
print datetime.date.today()
print mylist[0]
print mylist
