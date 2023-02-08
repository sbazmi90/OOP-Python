# The main class is here


class Vehicle:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f" Make: {self.make}\n Model: {self.model}\n year: {self.year}")



