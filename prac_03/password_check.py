PASSWORD_LENGTH = 5


def password_checker():
    """Get a password of valid size and print asterisks."""
    password = input("Enter password of at least {} characters: ".format(PASSWORD_LENGTH))
    while len(password) < PASSWORD_LENGTH:
        password = input("Enter password of at least {} characters: ".format(PASSWORD_LENGTH))

    print('*' * len(password))


password_checker()


# Break down functions

def main():
    """Print asterisks."""
    password = password_check(PASSWORD_LENGTH)
    print('*' * len(password))


def password_check(password_length):
    """Check password length"""
    password = input("Enter password of at least {} characters: ".format(password_length))
    while len(password) < password_length:
        print("Your pass word is too short")
        password = input("Enter password of at least {} characters: ".format(password_length))

    return password


main()
