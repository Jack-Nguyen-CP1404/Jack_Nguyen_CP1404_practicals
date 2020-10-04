from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Initialise SilverServiceTaxi instance based on parent class Taxi."""
    flag_fall = 4.50  # $

    def __init__(self, name, fuel, fanciness):
        self.fanciness = fanciness
        super().__init__(name, fuel)
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return "{}, plus flagfall of ${:.2f}".format(super().__str__(), self.flag_fall)

    def get_fare(self):
        """Calculate the current fare"""
        return super().get_fare() + self.flag_fall
