# Understanding methods inside functions

# class Fun_Math:
#     def __init__(self, char='*'):
#         print 'Inside init method'
#         self.char = char
#
#
#     def add(self, a, b):
#         print 'Inside add method'
#         return self.char * (a+b)
#
#
#     @staticmethod
#     def static_add(a,b):
#         print 'Inside static method'
#         a += 10
#         return '*' * (a+b)
#
# obj1 = Fun_Math('!')
# print obj1.add(2,3)
# print obj1.static_add(2,5)
#
# print Fun_Math('~').add(6,2) # '~' character sent as part of the function call.
# print Fun_Math.static_add(2*10,5)

# Another example of static method

# class Foo:
#     @staticmethod
#     def bar():
#         print 'bar'
#
#
# print Foo.bar
# print Foo().bar
# Foo.bar()
# Foo().bar()

class Box:
    def area(self):
        return self.w * self.h


    def __init__(self,w,h):
        self.w = w
        self.h = h


x = Box(10,2)
print (x.area())