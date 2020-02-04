# A Tuple is an immutable list and cannot be changed in any way once it is created.
# Adding or removing elements from a Tuple is not allowed.
# A tuple is defined in the same way as a list except that the whole set of elements are enclosed in () instead of [].

print '*****************************'

# Defining Tuple
tup = ('Vasai', 'Bhandup', 'Malad', 'Goregaon')
tup1 = (999,301,550,1001,408)
tup2 = ('Mulund', 'Thane', 'Dombivali')

print tup
print tup[0]
print tup[-1]
print tup[0:2]

print '*****************************'
# Using "in" operator to check if the value exists in Tuple
print "Naigaon" in tup
print "Vasai" in tup

print "Index of Malad is:",
print tup.index('Malad')

print '*****************************'

print "Length of Tuple is:",
print len(tup)

print '*****************************'

# Finding the maximum value based on alphabetical value
print "Maximum value in Tuple is: " + max(tup)
print "Maximum value in Tuple is:",
print max(tup1)

# Finding the maximum value based on alphabetical value
print "Minimum value in Tuple is: " + min(tup)
print "Minimum value in Tuple is:",
print min(tup1)

print '*****************************'

# 1 - Does not match
print cmp(tup, tup2)
print cmp(tup,tup1)

t1 = ('Python', 'Hadoop')
t2 = ('Python', 'Ruby')
t3 = ('Python', 'Hadoop')

# -1 - Second element of t2 is greater than second element of t1
print cmp(t1, t2)

# 1 - - Second element of t2 is greater than second element of t1
print cmp(t2, t1)

# 0 - Perfect match
print cmp(t1, t3)

print '*****************************'

# Creating new tuple by passing a sequence

tup3 = tuple(tup)
print tup3

# Creating a list by passing a asequence

li1 = list(tup3)
print li1

print '*****************************'

# Using enumerate tp print (index, value) of tup3
tup4 = tuple(enumerate(tup3))
print tup4[2]

print '***********THE END******************'