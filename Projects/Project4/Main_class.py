class Employee:

    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def calculate_pay(self):
        return self.salary


