# Dictionary is written as a series of key:value pairs seperated by commas, enclosed in curly braces{}.
# An empty dictionary is an empty {}.
# Dictionaries can be nested by writing one value inside another dictionary, or within a list or tuple.

print "--------------------------------"

# Defining dictionary
dic1 = {'c1':'Churchgate', 'c5':'Marine Drive', 'c4':'Vile Parle', 'c3':"Bandra", 'c2':'Dadar', 'c6':'Andheri'}
dic2 = {'w3':'Wadala', 'c5':'Chowpatty', 'w4':'Kurla', 'w5':"Thane", 'c2':'Dadar', 'w7':'Andheri'}

# Printing dictionary
print dic1

# Print all keys
print dic1.keys()

# Print all values
print dic1.values()

# Printing a particular value using key
print 'Value of key c4 is: ' + dic1["c4"]
print "Value of key c4 is: " + dic1.get("c4")

# Print all keys and values
print dic1.items()

print "--------------------------------"

# Add value in dictionalry
dic1['w1']='Victoria Terminus'
dic1['w2']=10001
dic1[20]='Byculla'
print dic1

print "--------------------------------"

# Finding data type of key
print [type(i) for i in dic1.keys()]

print "--------------------------------"
print "Length of dictionary is:",
print len(dic1)

print "--------------------------------"

# "in" used to test whether a key is present in the dictionary
print dic1
print 20 in dic1
print "c6" in dic1
print "c6" not in dic1

print "--------------------------------"

# Adding values in dictionary using another dictionary
# If same key exist in both the dictionaries then it will update the value of the key available from dic2 in dic1
# If both dictionaries have same key + value then it will only keep the original value from dic1

dic1.update(dic2)
print dic1

print "--------------------------------"

# Remove value from dictionary
dic1.pop('w4')
print dic1

print "--------------------------------"

# Looping through dictionary

for key, value in dic2.items():
    print key, value

print "--------------------------------"

dic1.clear()
print "Total number of elements in dic1 after using the clear function: ",
print len(dic1)

print "-------------THE END-------------------"