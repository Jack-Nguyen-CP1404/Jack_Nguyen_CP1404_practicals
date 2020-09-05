from prac_06.car import Car


def main():
    print("Let's drive!")
    car_name = input("Enter your car name: ")
    my_car = Car(car_name, 100)
    print(my_car)

    MENU = """Menu:
     d) drive
     r) refuel
     q) quit """
    print(MENU)
    choice = input("Enter your choice: ").lower()
    while choice != "q":
        if choice == "d":
            prompt_1 = "How many km do you wish to drive? "
            distance_driven = my_car.drive(valid_number_checker(prompt_1))
            if my_car.fuel == 0:
                print("The car drove {}km and ran out of fuel.".format(distance_driven))
            elif my_car.fuel > 0:
                print("The car drove {}km.".format(distance_driven))
            print(my_car)
        elif choice == "r":
            prompt_2 = "How many units of fuel do you want to add to the car? "
            added_fuel = my_car.add_fuel(valid_number_checker(prompt_2))
            print("Added {} units of fuel.".format(added_fuel))
            print(my_car)
        else:
            print("Invalid menu choice")

        print(MENU)
        choice = input("Enter your choice: ").lower()
    print("Good bye The bomb's driver.")


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
