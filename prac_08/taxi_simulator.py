from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.taxi import Taxi

Menu = """q)uit, c)hoose taxi, d)rive"""


def main():
    """Write a program using SilverServiceTaxi and Taxi classes.
     Allow users choose type of taxi and how far they want to drive,
    Display the trip cost and add it to their bill when user choose to quit."""
    total_fare = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive")
    print(Menu)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
        elif choice == "d":
            current_taxi.start_fare()
            driving_distance = float(input("Drive how far? "))
            current_taxi.drive(driving_distance)
            trip_fare = current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, trip_fare))
            total_fare += trip_fare
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(total_fare))
        print(Menu)
        choice = input(">>> ").lower()
    print("Total trip cost: ${:.2f}".format(total_fare))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display list of taxis."""
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
