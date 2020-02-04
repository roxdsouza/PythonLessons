import re
import urllib2

site = urllib2.urlopen(r'http://www.bsnl.co.in/opencms/bsnl/BSNL/about_us/contact_us.html')
text = site.read()

# Compile function can compile a regular expression pattern into pattern objects which can be used for matching.
# Using a pattern object and reusing it is more efficient when the expression is used
# multiple times in a single program.

urlstr = re.compile(r'http[s]*://[a-z|A-Z|0-9|.|/|~|?]+[.]+[a-z]+')
#emails = re.compile(r'[a-z|A-Z]+[a-z|A-Z|.|_|-|0-9]*@[a-z]+.[a-z|.]+')

emails = re.compile(r'[a-z|A-Z|.|_|-|0-9]*@[a-z]+.[a-z|.]+')

match = urlstr.search(text)
print '--------------------URLs---------------------'
print match.group()

print '--------------------Emails---------------------'
match = emails.search(text)
print match.group()