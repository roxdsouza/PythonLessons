import random

def random_num(option):
    rnum = 0
    if option == 'E':
        rnum = random.randint(1,10)
    elif option == 'I':
        rnum = random.randint(10, 100)
    elif option == 'H':
        rnum = random.randint(100, 200)
    return rnum


def add_function(option,questions):
    i = 1

    while i <= questions:
        num1 = random_num(option)
        num2 = random_num(option)
        ans = input(str(num1) + ' + ' + str(num2) + ' = ')

        if ans == (num1 + num2):
            print "That's right - well done!"
        else:
            print "The answer is incorrect!"
            print "The correct answer is: ", (num1 + num2)
        i += 1


def multi_function(option,questions):
    i = 1

    while i <= questions:
        num1 = random_num(option)
        num2 = random_num(option)
        ans = input(str(num1) + ' * ' + str(num2) + ' = ')

        if ans == (num1 * num2):
            print "That's right - well done!"
        else:
            print "The answer is incorrect!"
            print "The correct answer is: ", (num1 * num2)
        i += 1


def sub_function(option, questions):
    i = 1

    while i <= questions:
        num1 = random_num(option)
        num2 = random_num(option)
        ans = input(str(num1) + ' - ' + str(num2) + ' = ')

        if ans == (num1 - num2):
            print "That's right - well done!"
        else:
            print "The answer is incorrect!"
            print "The correct answer is: ", (num1 - num2)
        i += 1


def div_function(option, questions):
    i = 1

    while i <= questions:
        num1 = random_num(option)
        option = 'E'
        num2 = random_num(option)
        ans = input(str(num1) + ' / ' + str(num2) + ' (write only quotient) = ')

        if ans == (num1 / num2):
            print "That's right - well done!"
        else:
            print "The answer is incorrect!"
            print "The correct answer is: ", (num1 / num2)

        i += 1


choice = 'C'

while choice == 'C':
    option = raw_input("Choose level (Easy: E, Intermediate: I or Hard: H): ")

    if option in ('E', 'I', 'H'):
        questions = input("Please give us the number of questions you want to attempt: ")
        qtype = raw_input("Specify the question type (Multiplication: M, Addition: A, Subtraction: S, Division: D): ")

        if qtype == 'A':
            add_function(option,questions)
        elif qtype == 'M':
            multi_function(option,questions)
        elif qtype == 'S':
            sub_function(option,questions)
        elif qtype == 'D':
            div_function(option,questions)
        else:
            print 'Invalid option selected. Program terminated.'
            exit(1)
    else:
        print 'Invalid option selected. Program terminated.'
        exit(1)

    choice = raw_input('Continue: C or Exit: E - ')

    while choice not in ('C', 'E'):
        choice = raw_input('Continue: C or Exit: E - ')
        if choice == 'E':
            exit(0)
        elif choice == 'C':
            break
