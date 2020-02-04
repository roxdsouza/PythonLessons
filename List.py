# The list type is a container which holds a number of other objects, in a given order.
# List type implements the sequence protocol, and it allows you to add and remove objects from the sequence.
# A list is an ordered set of elements enclosed in square brackets.

# Defining a list
li = ['Sachin', 'Saurav', 'Shreeshant', 'Sameer', 'Suraj', 'Suzan', 'Swenson', 'Shane', 'Savio', 'Superman']

# Prints number of values in the list
print li

# Prints the total number of values in the list
print len(li)

# Prints the length of the ZERO element in the list
print len(li[0])

# Adds more elements to the list
li += ['Rocky', 'Russia']
print li
print len(li)

# Adds more elements to the list
li = li + ['Pradeep', 'Rahul']
print li
print len(li)

# Adding repeating elements to the list

li += ['Rohit'] * 3
print li

# Prints values between the 10th element to the 12th element in the list
print li[10:12]

# Prints all elements from the list using a FOR loop
for name in li:
    print name

# Prints the last element in the list
print li[-1]

print li

# Print from the 6th element to the second last element in the list
print li[6:-1]

# Prints elements from 0 to 4 from the list
print li[:5]

# Prints elements from 5 to the end of the list
print li[5:]

print "----------------------"
# LIST MANIPULATION METHODS

# New list variable
li1 = ['Simon', 'Sheetal', 'Suresh']

# Adding elements of one list to another list
li.extend(li1)
print li
print li1

print "----------------------"

# Append adds only one element to the end of the list
li.append('Albert')
li.append('Amir')
li.append('Smarak')

print li

print "----------------------"

# Inserts an item at a given position of the list
li.insert(0, 'Rahul')
li.insert(10, 'Kiran')
print li

print "----------------------"

# Find the first occurrence of a lalue in the list and returns the index
li.insert(9, 'Sameer')
print li
print li.index('Sameer')

print "----------------------"

# "in" used to test whether a value is present in the list
print "Kiran" in li

# Returns False if the value is NOT present in the list
print "Anthony" in li

print "----------------------"

# Remove element from the list
li.pop(0)
print li

print "----------------------"

# Remove first occurance from the list
li.remove("Sameer")
print li

print "----------------------"

# Reverse elements in the list
li.reverse()
print li

print "----------------------"
# This just displays the list in reverse order but does not change the list itself
print li[::-1]
print li

print "----------------------"

# Prints values in the reversed order using FOR loop and REVERSE() function
for name in reversed(li):
    print name

print li

print "---------THE END-------------"