from prac_06.guitar import Guitar


def main():
    """Write guitar program to ask for user input, use Guitar class"""

    print("My guitars!")
    guitar_list = []
    name = input("Enter guitar's name: ")
    # Write while loop to allow user to enter inputs until empty string is entered

    while name != "":
        prompt_1 = "Enter year: "
        year = int(valid_number_checker(prompt_1))
        prompt_2 = "Cost: $"
        cost = valid_number_checker(prompt_2)
        guitar = Guitar(name, year, cost)
        guitar_list.append(guitar)
        print("{} added".format(guitar))
        name = input("Enter guitar's name: ")

    max_length = max(len(guitar.name) for guitar in guitar_list)

    for i, guitar in enumerate(guitar_list):

        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(Vintage)"
        print("Guitar {}: {:{}} ({}), worth ${:10,.2f} {}".format(i + 1, guitar.name, max_length, guitar.year,
                                                                  guitar.cost, vintage_string))


def valid_number_checker(number):
    """Check user input to make sure it is a positive integer and use "try" and "exception" to continue the program
    even when user enter an input other than an integer."""

    user_error = False
    while not user_error:
        try:
            user_input = float(input(number))
            if user_input > 0:
                user_error = True
                return user_input
            elif user_input < 0 or user_input == 0:
                print("Number must be > 0")
        # Avoid crashing the program when user enter a string
        except ValueError:
            print("Invalid input; enter a valid number")
    return user_input


main()
