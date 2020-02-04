import os

# print "============================"
#
# print os.path.abspath('.') # Display the current working directory
# print os.path.abspath('..') # Displays one directory behind
#
# os.chdir('C:\TEMP\A1\Test03')
# print os.path.abspath('.')
# print os.path.abspath(r'sample01') # Partial path relative to cwd. Does not actually change directory.
# print os.getcwd()
# print os.path.abspath('..\..')
# print os.getcwd()
# print 'Absolute - ' + os.path.abspath('.')
# print os.path.abspath(r'C:\TEMP\A1\Test03\Sample01')
# print 'Absolute - ' + os.path.abspath('.')
#
# os.chdir('C:\TEMP\A1')
# print 'Absolute - ' + os.path.abspath('.')
# print os.path.abspath(r'C:\TEMP\A1\Test03\Sample01')
# print 'Absolute - ' + os.path.abspath('.')

print '================================'

# Other os.path functions

# Join takes one or more paths and joins them by using the current operating systems path separator
print os.path.join('C:\TEMP\A1\Test03\Sample01', 'C:\TEMP\A1')

# Takes path name and returns true if it exists

print os.path.exists('C:\TEMP\A1\Test03\Sample01')

# Takes a pathname and returns true if it points to a directory

print os.path.isdir('C:\TEMP\A1\Test03\Sample01')
print os.path.isdir('C:\TEMP\New-File01.txt')

# Takes a file name and returns true if the file exists
print os.path.isfile('C:\TEMP\New-File1.txt')

# Split takes a pathname and returns it in two parts: the directory part and the filenmae
print os.path.split('C:\TEMP\New-File1.txt')
print os.path.split('C:\TEMP\A1\Test03\Sample01')

# Normpath converts path names in non standard formats to standard format
print os.path.normpath('C:\TEMP\A1/\\Test03\Sample01')
print os.path.normpath('C:\TEMP\A1/\Test03\Sample01')