# class Vector:
#     def __init__(self, data):
#         self.data = data
#         # print 'Data: ' + str(data)
#         # print 'Length: ' + str((len(self.data)))
#         # print self.data
#
#
#     def __str__(self):
#         return repr(self.data)
#
#
#     def __add__(self, other):
#         # print 'Inside add...'
#         data = []
#         for j in range(len(self.data)):
#             data.append(self.data[j] + other.data[j])
#
#         return Vector(data)
#
#
#     def __sub__(self, other):
#         data = []
#         for j in range(len(self.data)):
#             data.append(self.data[j] - other.data[j])
#
#         return Vector(data)
#
#
# x = Vector([1,2,3])
# y = Vector([6,0,2])
#
# print x + y
# print y - x

class Vector:
    def __init__(self, data):
        self.data = data


    def __str__(self):
        return repr(self.data)


    def __sub__(self, other):
        data = []
        for j in range(len(self.data)):
            data.append(self.data[j] - other.data[j])

        return Vector(data)


x = Vector([2,5])
y = Vector([15,25])

print y - x