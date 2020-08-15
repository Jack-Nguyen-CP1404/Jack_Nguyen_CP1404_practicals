PASSWORD_LENGTH = 5
password = input("Enter the password: ")
if len(password) <= PASSWORD_LENGTH:
    print(("*" * len(password)))
else:
    print(("Your password is: {}".format(password)))
