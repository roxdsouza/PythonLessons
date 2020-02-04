import sys

# FORMAT
# try:
#   data = something-that-can-go-wrong
#
# except IOError:
#   handle_the_exception_error
#
# else: # Should be toward the end of the try and except statement
#   doing_different_exception_handling
# You can use the "PASS" keyword if nothing needs to be done in the else statement
#
# finally: # FINALLY clause is optional and is intended to define clean-up actions that must be executed under
#          # all circumstances whether an exception has occurred or not.
#          # The FINALLY clause is always executed before leaving the try statement.
# print 'Goodbye!'

# IOError - If the file cannot be opened
# ImportError - If Python cannot find the module
# ValueError - Raised when a built-in operator or function receives an argument that has the right type but
# an inappropriate value
# KeyboardInterrupt - Raised when the user hits the interrupt key (ctrl+c)
# EOFError - Raised when one of the built-in function (input() or raw_input()) hits an end-of-file condition
# (EOF) without reading any data

print '-------------------------------'
print 'Adding try and except block in the code'

try:
    number = input("Enter a number between 1 - 10\n")
except NameError:
    print 'Error! Numbers are only allowed.'
    sys.exit()

print 'The number entered by you is: ', number
