import re

# class Account:
#     def __init__(self, id):
#         self.id = id
#         id = 666
#
#
# acc = Account(123)
# print (acc.id)

################################################
# class Person:
#     def __init__(self, id):
#         self.id = id
#
#
# obama = Person(100)
# obama.__dict__['age'] = 49
# print (obama.age + len(obama.__dict__))

################################################
#
# class A:
#     def __init__(self, a,b,c):
#         self.x = a + b + c
#
#
# a = A(1,2,3)
# b = getattr(a, 'x')
# print b
# setattr(a, 'x',b+1)
# print (a.x)

################################################
# class NumFactory:
#     def __init__(self,n):
#         self.val = n
#
#
#     def timesTwo(selfself):
#         self.val *= 2
#
#
#     def plusTwo(self):
#         self.val += 2
#
#
# f = NumFactory(2)
# print dir(f)
# for m in dir(f):
#     mthd = getattr(f,m)
#     if callable(mthd):
#         mthd()
#
#
# print(f.val)

# t="A fat cat doesn't eat oat but a rat eats bats."
# mo = re.findall("[force]at", t)
# print (mo)

a = re.findall('..$', 'aeroplane')
b = re.findall('^.', 'computer')

print a, b