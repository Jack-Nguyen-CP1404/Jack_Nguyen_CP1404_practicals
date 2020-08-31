def main():
    address_dict = {}
    MENU = """    E - Enter a new name & address
    C - Change an address for an existing entry
    P - Print the address for a name you choose
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":

        if choice == "E":
            info = name_address()
            name = info[0]
            address = info[1]
            print(name, address)
            address_dict[name] = address
        elif choice == "C":
            name = input("Enter a friend's name you want to change address: ")
            address_dict[name] = input("Input your friend's new address: ")
            print(address_dict)
        elif choice == "P":
            name = input("Enter a name you want to print: ")
            print("{} is at {}".format(name, address_dict[name]))
        print(MENU)
        choice = input(">>> ").upper()
    else:
        print("Invalid menu option")


def empty_string_checker(string):
    """Keep asking user to input a string when an empty string is entered"""

    while string == "":
        print("Input can not be blank")
        string = input("Name: ")
    return string


def name_address():
    name = input("Enter your friend's name: ")
    empty_string_checker(name)
    address = input("Enter your friend's address: ")
    empty_string_checker(address)
    return name, address



main()
