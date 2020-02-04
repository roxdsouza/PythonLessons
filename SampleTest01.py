# increment = lambda num, incr=5: num + incr
#
# print increment(5, 10)
#
# from operator import itemgetter
# increment = lambda mylist: sorted(mylist, key=itemgetter(1,0))
#
# mylist = [['john', 1, 'a'], ['larry', 0, 'b']]
#
# print increment(mylist)

#
# print '----------------------------'
#
# def recur(a):
#     if not a:
#         return 0
#     else:
#         return a[0] + recur(a[1:])
#
# print recur([1,2,3,4,5])
#
# print '-----------------------------'
#
#
# def recur(x, n):
#     if n == 1:
#         return x
#     else:
#         print n
#         return x * recur(x, n - 1)
#
#
# print recur(4, 4)
#
# def f(a, b):
#     print(a, b)
#
#
# f(b=1,*(2,))
#
# ----------------------------

# def f(a):
#     pass
#
#
# f(a for a in [1, 2])
#
# colors = ["blue", "lavender", "red", "yellow"]
#
# for color in sorted(colors, key=lambda color: len(color), reverse=True):
#       print(color)
#
# furniture = {"table" : 1, "chair" : 2, "desk" : 4}
# s = sorted(furniture.keys())
# for key in s:
#       print(key, furniture[key])
#
# import datetime
# now = datetime.datetime(2003, 8, 4, 12, 30, 45)
# print now.month

import datetime
print datetime.datetime.strptime('January 11, 2010', '%B %d, %Y').strftime('%A')