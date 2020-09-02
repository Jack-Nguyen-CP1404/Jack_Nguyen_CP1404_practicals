def main():
    """Ask user for their email and pack their name and email address in email_dict"""

    user_emails = input("Email: ")
    email_dict = {}
    email_to_name(user_emails)
    while user_emails != "":
        user_name = email_to_name(user_emails).title()
        user_name_confirmation = input("Is your name {}? (Y/N) ".format(user_name)).upper()
        if user_name_confirmation != "" and user_name_confirmation != "Y":
            user_name = input("Enter your name: ").title()
        email_dict[user_emails] = user_name
        user_emails = input("Email: ")

    # User for loop to print out user emails and their name from email_dict
    for user_emails, user_name in email_dict.items():
        print("{} ({})".format(user_name, user_emails))


def email_to_name(user_email):
    """Split name out of user email address"""

    name_parts = user_email.split('@')[0]
    user_name = " ".join((name_parts.split(".")))
    return user_name


main()
