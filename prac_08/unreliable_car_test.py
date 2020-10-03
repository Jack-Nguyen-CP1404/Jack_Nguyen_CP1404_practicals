from prac_08.unreliable_car import UnReliableCar


def main():
    """Test unreliable cars"""
    reliable_car = UnReliableCar("Fair car", 100, 80)
    unreliable_car = UnReliableCar("Bad car", 100, 10)
    # Use a for loop to generate number of times attempt to drive the car
    for i in range(1, 10):
        print("Attempt {}: drive {}km".format(i, i))
        print("{:{}} drove {:2}km".format(reliable_car.name, len(reliable_car.name), reliable_car.drive(i)))
        print("{:{}} drove {:2}km".format(unreliable_car.name, len(reliable_car.name), unreliable_car.drive(i)))

    # print name, fuel and distance travelled of the cars
    print(reliable_car)
    print(unreliable_car)


main()
