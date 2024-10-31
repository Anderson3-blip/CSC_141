class car:
    """A simple attempt to represent a car."""


def __init__(self, make, model, year):
    """Intialize attributes to describe a car."""
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0

def get_descriptive_name(self):
    """Return a neatly formatted descriptive name."""
    long_name = f"{self.year} {self.make} {self.model}"
    return long_name.title()

def read_odometer(self):
    """Print a statement showing car's mileage."""
    print(f"This car has {self.odometer_reading} miles on it.")

def update_odometer(self, mileage):
    """Set the odometer reading to the given value."""
    if mileage >= self.odometer_reading:
        self.odometer_reading = mileage
    else:
        print("You can't roll back an odometer!")

def increment_odometer(self, miles):
    """Add the given amount to the odemeter reading."""
    self.odometer_reading += miles

class ElectricCar(car):
    """Represent aspects of a car, specific to electric vehicles."""

def _init_(self, make, model, year):
    """Intialize attributes of the parent class."""
    super()._init_(make, model, year)

my_leaf = ElectricCar(Car):
