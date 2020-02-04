# print '------------------------'
#
# a = range(10)
# print a
#
# print 'Using the sort function but not actually changing the value of a: '
# print sorted(a, reverse=True)
# print a
#
# print '------------------------'
# print "Actually changing the values of a by sorting in reverse order: "
# a.sort(reverse=True)
#
# print a

from operator import itemgetter
print 'Using the itemgetter function'
mylist = [['john', 1, 'a'], ['larry', 0, 'b']]
print mylist
print sorted(mylist, key=itemgetter(1,0))

print '-----------THE END--------------'
