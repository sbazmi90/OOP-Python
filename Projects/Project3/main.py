


if __name__ == '__main__':
    from pattern import *

    vehicles = [Car("Toyota", "Camry", 2020, 4),
                Motorcycle("Honda", "GP", 2021, 2),
                Boat("Bayliner", "SX", 2022, 1)]

    for v in vehicles:
        v.display_info()

