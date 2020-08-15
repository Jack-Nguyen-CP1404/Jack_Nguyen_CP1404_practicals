# Menu-driven number sequence generator:

x = int(input("Enter starting integer number: "))
y = int(input("Enter ending integer number: "))
menu = """E - Even number display from x - y
O - Odd number display from x - y
S- Squares from x- y
Q- Quit"""
print(menu)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "E":
        for i in range(x, y, 2):
            if (x % 2) == 0:
                print(i, end=' ')
            else:
                print(i+1, end=' ')
    elif choice == "O":
        for i in range(x, y, 2):
            if (x % 2) == 1:
                print(i, end=' ')
            else:
                print(i+1, end=' ')
    elif choice == "S":
        for i in range(x, y+1, 1):
            c = pow(i, 2)
            print(c, end=' ')
    else:
        print("Invalid option")
    print()
    print(menu)
    choice = input(">>> ").upper()

