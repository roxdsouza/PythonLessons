import os

# FILE MODES
# ===========
# r - read-only mode
# a - append the file
# rb - read file in binary mode. File pointer is placed at the BOF. This is the default mode
# w - write mode. Creates new file if it does not exist. Overwrites the file if it exists.
# r+ - Opens file for reading and writing. File pointer is at BOF.
# w+ - read and write mode. Creates new file if it does not exist. Overwrites the file if it exists.
# rb+ - Opens file for reading and writing in binary format. File pointer is at BOF.
# wb - write only in binary mode. Creates new file if it does not exist. Overwrites the file if it exists.
# wb+ - read and write in binary format. Creates new file if it does not exist. Overwrites the file if it exists.
#
# print "============================"
#
# # Deleting an existing file
#
# exists = os.path.isfile("c:\TEMP\New-File1.txt")
# if exists:
#     os.remove("c:\TEMP\New-File1.txt")
#     print "Deleted existing file."
# else:
#     pass
#
# print "============================"
#
# # Delete existing directory
#
# exists = os.path.isdir("c:\TEMP")
# if exists:
#     os.rmdir("c:\TEMP")
#     print "Temp directory deleted."
# else:
#     pass
#
# print "============================"
#
# # Create new directory
#
# exists = os.path.isdir("c:\TEMP1")
# if not exists:
#     os.mkdir("c:\TEMP1")
#     print "Temp directory created."
# else:
#     pass
#
# print "============================"
#
# # Renaming directory
#
# exists = os.path.isdir("c:\TEMP1")
# if exists:
#     os.rename("c:\TEMP1", "c:\TEMP")
#     print "Directory renamed."
# else:
#     pass
#
# # Change directory and get current working directory
#
# os.chdir("c:\TEMP")
# print os.getcwd()
#
# print "============================"
#
#
#
# # Creating a new file and opening it in a write mode
# print "============================"
# print "Creating a new file"
# newFile = open("C:\TEMP\File1.txt", "w")
#
# print "Writing to a file"
# newFile.write("Good Morning! \n")
# newFile.write("Today we are going to Wild Wild Wet!!!")
#
# print "File was opened in:",
# print newFile.mode
#
# print "File name is:",
# print newFile.name
#
# print 'Is the file closed?',
# print newFile.closed
#
# print "Closing the file."
# newFile.close()
#
# print 'Is the file closed?',
# print newFile.closed
#
# print "============================"
# print "Opening file in a read-only mode"
# newFile = open("C:\TEMP\File1.txt", "r")
#
# print "Reading contents of the file"
# print newFile.read()
#
# # Tell function tells the current pointer position within the file.
# print newFile.tell()
#
# # Moving the file pointer to a certain position in the file. seek(0) will move the pointer to BOF.
# # Seek([offset],[from]) - from has 3 values. 0 - BOF, 1 - Current position and 2 - EOF.
#
# newFile.seek(32)
# newFile.seek(-16, 1)
# print newFile.read()
#
# newFile.close()
#
# print "============================"
#
# # Need to import os for the following functions to work.
#
# print 'Renaming a file'
# os.rename("c:\TEMP\File1.txt", "c:\TEMP\New-File1.txt")
#
# print "============================"
#
# print "Print names of files in this directory: "
# print os.listdir('.')
#
# print 'Number of files in the current directory: '
# print len(os.listdir('.'))

# print "============================"
#
# # The method makedirs() is recursive directory creation function. Like mkdir(),
# # but makes all intermediate-level directories needed to contain the leaf directory.
#
# print "Create multiple directories"
# os.makedirs('c:\TEMP\A1\Test01')
# os.makedirs('c:\TEMP\A1\Test02')
# os.makedirs('c:\TEMP\A1\Test03\Sample01')

# os.removedirs('c:\TEMP\A1\Test03\Sample01')

