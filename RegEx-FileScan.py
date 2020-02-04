# Program to read ALL Yahoo email addresses from a text file
# To replace gmail with tmail and write back to the file

import re
import os

print "Creating file."

f = open("c:\TEMP\email.txt", "w")

f.write("sachin@yahoo.com \n")
f.write("tendulkar@yahoo.co.in \n")
f.write("manish@gmail.com \n")
f.write("michael@aol.com \n")
f.write("pravin@gmail.com \n")
f.write("tejas@gmail.co.in \n")
f.write("mitesh@gmail.com \n")
f.write("suresh@yahoo.com \n")
f.write("prabhu@gmail.co.sg \n")
f.write("manisha@hotmail.com \n")
f.write("manisha@microsoft.com")

f.close()
print "File closed."

f = open("c:\TEMP\email.txt", "r")

print "Reading file."

gmails = re.findall(r'[\w\.-]+@yahoo[\w\.-]+', f.read())

for email in gmails:
    print email

f.seek(0)
all_mails = re.sub('gmail', 'tmail', f.read())
print "Substituting gmail to tmail."

f.close()

print "File closed."

f = open("c:\TEMP\email.txt", "w")

print "Writing to file."
f.write(all_mails)

print "File closed."
f.close()

print '-----------Done-------------'