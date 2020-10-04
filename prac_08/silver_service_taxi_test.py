from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Test function for class SilverServiceTaxi"""
    fancy_taxi_1 = SilverServiceTaxi("Hummer taxi", 200, 4)
    print(fancy_taxi_1)
    # Test for 18km trip with fancy of 2
    fancy_taxi_2 = SilverServiceTaxi("BMW", 100, 2)
    fancy_taxi_2.drive(18)
    print(fancy_taxi_2)
    print("{:.2f}".format(fancy_taxi_2.get_fare()))


main()
