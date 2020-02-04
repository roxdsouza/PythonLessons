# Program to understand class and instance variables

# class Edureka:
#
#     # Defining a class variable
#     domain = 'Big data analytics'
#
#     def SetCourse(self, name):  # name is an instance variable
#         # Defining an instance variable
#         self.name = name
#
#
# obj1 = Edureka() # Creating an instance of the class Edureka
# obj2 = Edureka()
#
# print obj1.domain
# print obj2.domain
#
# obj1.SetCourse('Python') # Calling the method
# obj2.SetCourse('Hadoop')
#
# print obj1.name
# print obj2.name


########################################################

# Program to understand more about constructor or distructor

class Edureka:
    def __init__(self, name):
        self.name = name


    def __del__(self): # Called when an instance is about to be destroyed
        print 'Destructor started'


obj1 = Edureka('Python')
obj2 = obj1

# Calling the __del__ function

del obj1
obj1 = obj2
print obj2.name
print obj1.name
del obj1, obj2