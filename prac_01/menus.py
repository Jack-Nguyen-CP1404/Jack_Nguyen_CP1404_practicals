name = input("Enter your name: ")
menu = """H - Say hello
G - Say goodbye
Q- Quit """
print(menu)
choice = input(">>>").upper()
while choice != "Q":
    if choice == "H":
        print("Hello " + name)
    elif choice == "G":
        print("Goodbye " + name)
    else:
        print("Invalid choice")
    print(menu)
    choice = input(">>>").upper()
