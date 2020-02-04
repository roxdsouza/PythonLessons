# Program to understand how to use classes

# Built-in Class Attribute
# __dict__ : Dinctionary containing the class namespaces
# __doc__ : Class documentation string or None if defined
# __name__ : Class name
# __module__ : Module name in which the class is defined
# __bases__ : A possibly empty tuple contaning the base classes,
# in the order of their occurrence in the base class list.

# Private: attributes can only be accessed inside of the class definition (Naming: __name) \
# It is nether possible to read nor write to those attributes, except inside the class definition itself
# Protected :(restricted) attributes should only be used under certain conditions (Naming: _name) \
# Should not be used outside of the class definition, unless inside of a subclass definition
# Public : attributes can and should be freely used inside or outside the class definition (Naming: name)


class Not_So_Empty:

    a = 10 # This is a class variable and is common for all instances

    def __init__(self, param1=42): # param1 get value 100 when called for obj2
        print "Class initiated."
        self.b = param1 # Variable b is an object variable and value for this can be set while calling the class


print Not_So_Empty.a # Directly accessing class object
# print Not_So_Empty.b

obj1 = Not_So_Empty()
obj2 = Not_So_Empty(100)
print (obj1.a, obj1.b), (obj2.a, obj2.b)
print dir(Not_So_Empty)

obj2.p = 'What?' # This belongs to only obj2
Not_So_Empty.g = 100 # This is automatically available for objects 1, 2 and 3
print obj2.p

obj3 = Not_So_Empty()
print obj1.g, obj2.g, obj3.g