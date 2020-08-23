NUM = 7
USERNAMES = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


def main():
    print_statements()
    username_checker()


def numbers_list():
    """Append input numbers into numbers list"""
    numbers = []
    count = 1
    while count <= NUM:
        number = int(input("Enter number: "))
        count += 1
        numbers.append(number)
    return numbers


def print_statements():
    """Print first number, last number, smallest, largest number and average number from input numbers"""

    data = numbers_list()
    print("First number is {}".format(data[0]))
    print("The last number is {}".format(data[-1]))
    print("The smallest number is {}".format(min(data)))
    print("The largest number is {}".format(max(data)))
    print("The average number is {}".format((sum(data) / len(data))))


def username_checker():
    """Ask user for their username, if the name is in above list of authorised users, print "Access granted",
    otherwise print "Access denied". """

    username = input("Enter your name: ")
    if username in USERNAMES:
        print("Access granted")
    else:
        print("Access denied")


main()
