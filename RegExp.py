import re

# re module is used for regular expression
# Documentation - https://docs.python.org/2/library/re.html
# Examples - https://www.guru99.com/python-regular-expressions-complete-tutorial.html

# "\d" matches any digit; "\D" matches any non digit.
# "\s" matches any whitespace character; '\S" matches any non-alphanumeric character.
# "\w" matches any alphanumeric characters; "\W" matches any non-alphanumeric character.
# "^" matches the beginning of the string; "$" matches the end of the string.
# "\b" matched a word boundary; "\B" matches position that is not a word boundary.

# x|y matches x or y
# x* matches zero or more x's
# x+ matches one or more x's
# x? matches zero or one x's
# x{m,n} matches i x's, where m<i<n. Example >> "d{2,3}" matches "dd" or "ddd"

text = 'Game of Thrones is roughly based on the storylines of A Song of Ice and Fire, set in the fictional \
Seven Kingdoms of Westeros and the continent of Essos. The series chronicles the violent dynastic struggles among \
the realm\'s noble families for the Iron Throne, while other families fight for independence from it. It opens with \
additional threats in the icy North and Essos in the east.'

# print ('---------------SEARCH / MATCH FUNCTION---------------')
# print re.search('Game', text) #Just returns the MATCH object for the first instance of the match within a string
# match = re.search('Game', text)
# print match.group()
# print re.match('Game', text) #Searches for the word at the begining of the string and returns a MATCH object.
# print re.match('is', text)
#
# print ('---------------FIND ALL---------------')
# print re.findall('the', text) #Searches for ALL the instances of the word in the entire string
# print len(re.findall('the', text))
#
# print re.findall(r'noble|icy|power', text) #using the OR operator. r - means raw string.
# print re.findall(r'i[a-z]*', text) #Find all words contains 'i' and the rest of the word
# print re.findall(r'i[a-z]+', text) #Find all words contains 'i' and the rest of the word
#
# print re.findall(r'i[a-z].', text) # '.' means show one character after match
# print re.findall(r'\bi[a-z]\b', text) #Find 2 letter words starting with 'i'
# print re.findall(r'\ba[a-n|p-z]*\b', text) # Ignores words starting with 'a' but contains 'o'
# print re.findall(r'\ba[^o]*\b', text) # Ignores words starting with 'a' but contains 'o'
# print re.findall(r'^\w+', text) # Matches the start of a string
# print re.findall(r'\bf[a-z]*\b', text) # Searches for words that start with 'f'
#
# print ('---------------MATCH OBJECT---------------')
# r = re.search('violent', text)
# print r.group() # Returns the string that matched
#
# print 'Starting location of the index', r.start()
# print 'Ending location of the index', r.end()
# print 'Start and end location of the index (returns in Tuple)', r.span()
#
# # r = re.search('final', text) #Trying to find a non-existent word and it throws an exception.
# # print r.group() # Returns the string that matched
#
# m = re.match(r"(..)+", "edureka") # This matches every 2 consecutive characters - ed, ur, ek.
# # 'a' is left out as it does not have a pair.
# print m.group(1) # Returns only the last match i.e. ek
#
# # Another example
#
# var = "I work at Edureka, and thomas@edureka.in is my email id."
# domain = re.search(r'[\w.]+@[\w.]+', var)
# print (domain.group())

# DatePattern = 'There are multiple date patterns. Some of them are 01-01-2019, 01-Jan-2019, 2019-01-01, 01/01/2019, 01 Jan 2019, 01-01-19, etc.'
#
# # r = re.search(r'\b[\d]*|-|[\d.]|-|[\d.]\b', DatePattern)
# r = re.search(r'[\d]{4}-[\d]{2}-[\d]{2}', DatePattern)
# print (r.group())

# # Verify SSN number assuming the format is XXX-XX-XXXX
#
# SSNData = "Social security number of Michael Clarke is 724-132-8761"
# r = re.search(r'[\d]{3}-[\d]{3}-[\d]{4}', SSNData)
# print (r.group())
#
# Program to find a particular e-mail address
# Emails = "sachin@yahoo.com, tendulkar@yahoo.co.in, michael@aol.com, pravin@gmail.com, manisha@microsoft.com, "\
# "mitesh@gmail.com, tejas@gmail.co.in, manoj@microsoft.com"
# pick = re.findall(r'[\w\.-]+@microsoft[\w\.-]+', Emails)
#
# for mails in pick:
#     print mails

# Program to find IPv4 addresses
IPaddr = "Here are a few samples of IPv4 addresses: 192.0.2.1, 172.16.254.1, 192.168.1.15, 255.255.255.255, 10.142.0.2"
addr = re.findall(r'[\d]{1,3}.[\d]{1,3}.[\d]{1,3}.[\d]{1,3}', IPaddr)

for IPtext in addr:
    print IPtext