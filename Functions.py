# Working with functions

import hashlib

# def my_first_function(name):
#     print "Hello " + name + "!!!"
#
# my_first_function("Rox")
#
# print ("---------------------")
#
# def get_hash(name):
#     my_first_function(name)
#     return hashlib.sha224(name).digest()
#
# a = get_hash("Ganesh")
# print a
#
# print ("---------------------")
#
# def manipulate(a_list, b = 10):
#     print a_list
#     a_list.append(b) # Changing value permanently by using the manipulative function
#     print a_list
#     a_list.pop(1)
#     print a_list
#     return a_list
#
# def safe_func(a_list, b=10):
#     print a_list
#     a_list.pop(2)
#     print a_list
#     a_list = a_list + [b] # Changing value temporarily by using assignment "="
#     print a_list
#     return a_list
#
# z = [1,2,3]
#
# safe_func(z)
# print 'While safe :', z
#
# manipulate(z)
# print 'While referencing the same object: ',z
#

# print ("---------------------")
#
# # Learning about LEGB (Local, Enclosed, Global, Builtin)
#
# # Priority for functions:
# # Local - Will search for a variable in a local function first
# # Enclosed - Next will search for a variable in a level above. In example below - "outer_function", variable a
# # Global - Next will search for a variable in the program. In example below - variable z
# # Builtin - If nowhere found then it will search in builtin functions. Eg __name__
#
# a = 10
# z = 100
#
# def outer_function(param1):
#
#     a = 15
#     b = 20
#
#     def inner_function():
#         b = 56
#         print a, b, param1, z, __name__
#
#     inner_function()
#
# outer_function(1000)
#
# print ("---------------------")
#
# varGlobal = 10
#
# def fun():
#
#     global varGlobal
#     varLocal = 0
#
#     print 'Value of varGlobal: ',
#     print varGlobal
#     varGlobal = 0
#
# fun()
#
# if varGlobal == 0:
#     print 'Flag was set to 0, hence code was executed successfully!'
#
# print ("-------POSITIONAL PARAMETERS--------------")
#
#
# def jumbled(a, b, c=55):  # c has default value of 55. If nothing is passed then it will take the default value.
#     print a, b, c
#
#
# jumbled(10, 20, 30)  # Values assigned automatically to variables a, b and c
# jumbled(10, c=30, b=20)  # Named values passed. Unnamed values should be passed first (for eg value of a)
# jumbled(c=30, a=10, b=20)
# jumbled(b=20, a=10)  # Default value is assigned to c
#
# # jumbled(c=30,10,a=20) # This will result in an error as unnamed values have to be passed first

# print ("---------ARBITARY ARGUMENTS------------")
#
# def concat(*args):  # In case we don't know how many arguments a function is going to receive
#
#     for i in args:
#         print i
#     return " + ".join(args)
#
#
# print concat("Python", "Anaconda", "IronPython","Hello")
#
# print ("---------------------")
#
# print "----------NAMED ARGUMENTS--------------"
#
# # what if you want named arguments but don't know how many of them?
# # Single * creates a list (as in the above example) and ** creates a dictionary
#
# def print_team(teamname, **kargs):
#     print '****************' + teamname + '*****************'
#     print kargs # kargs is a dictionary
#     for k, v in kargs.items():
#         print k + ' : ' + v
#
#
# # print_team(teamname='Voyager', manager='Gupta', player1='John Doe', player2='Jane Doe')
# print_team(teamname='Voyager', manager='Gupta', player1='John Doe', player2='Jane Doe')
#
# print '-----------------------'
# def print_everything(*args):
#     for count, thing in enumerate(args):
#         print ('{0}.{1}'.format(count, thing))
#
# print_everything('Edureka','Python','Language')

print('-----------FUNCTION RETURNING A FUNCTION---------------')

def linear_equation(slope, c=0):
    print '1'
    def equation(x):
        print '3'
        return slope*x + c
    print '2'
    return equation

eq1 = linear_equation(slope=3, c=5)
print type(eq1)
print eq1

print eq1(5)