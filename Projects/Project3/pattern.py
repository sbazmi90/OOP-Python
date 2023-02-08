# For other subclasses that inherits from the main class

from vehicle import *

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of door: {self.num_doors}")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)
        self.num_wheels = num_wheels

    def display_info(self):
        super().display_info()
        print(f"Number of wheels: {self.num_wheels}")


class Boat(Vehicle):
    def __init__(self, make, model, year, num_propellers):
        super().__init__(make, model, year)
        self.num_propellers = num_propellers

    def display_info(self):
        super().display_info()
        print(f"Number of propellers: {self.num_propellers}")


