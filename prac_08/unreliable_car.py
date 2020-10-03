from random import randint
from prac_08.car import Car


class UnReliableCar(Car):
    """Create an unreliable version of car"""

    def __init__(self, name, fuel, reliability):
        """Initialise a UnReliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Only allow the car to drive when the the random number is less than reliability"""
        random_number = randint(0, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
