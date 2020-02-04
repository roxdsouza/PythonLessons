# Program to calculate distance
#
# class Calculate_Distance:
#
#     def __init__(self, start1, start2):
#         self.start1 = start1
#         self.start2 = start2
#
#
#     def calc_distance(self, end1, end2):
#         return (end1 - self.start1) + (end2 - self.start2)
#
#
# point1 = Calculate_Distance(2,5)
# print (point1.calc_distance(12,15))

########################################################################
class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def __str__(self):
        return "x-value: "+ str(self.x) + " y-value " + str(self.y)


    def __add__(self, other):
        p = Point()
        p.x = self.x + other.x
        p.y = self.y + other.y
        return p


p1 = Point(3, 4)
p2 = Point(2, 3)
print (p1 + p2)
