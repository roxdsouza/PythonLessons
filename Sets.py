# Sets are unordered collections of uniques and immutable objects.
# Sets are created by calling the built-in set function.

print "======================================"
# Defining sets

s1 = set("Hello")
s2 = set("World")
s3 = set("Good Morning")

print s1, s2, s3

print "======================================"
# UNION - Adding two sets

print "Union of 2 sets: ",
print s1|s2
print "Union of 3 sets:",
print s1|s2|s3
print s1.union(s2,s3)

print "======================================"
# INTERSECTION - Takes only common values

print "Intersection of 2 sets: ",
print s1&s2
print "Intersection of 3 sets: ",
print s1&s2&s3
print s1.intersection(s2,s3)

print "======================================"
# DIFFERENCES

print "Differences of 2 sets - S1: ",
print s1-s2
print "Differences of 2 sets - S2: ",
print s2-s1
print "Differences of 3 sets: ",
print s1-s2-s3
print s1.difference(s2,s3)

print "===================THE END==================="