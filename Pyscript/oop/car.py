class Car:
    """As simple attempt to represent a car"""
    def __init__(self, make, model, year):
        """Initialize attributes to describe the car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles
        
my_new_car = Car('audio','a4',2019)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(45)
print(my_new_car.read_odometer())
