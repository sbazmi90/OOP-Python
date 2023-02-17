

from Main_class import Employee


class Manager(Employee):

    def __init__(self, name, id, salary, bonus):
        super().__init__(name, id, salary)
        self.bonus = bonus


    def calculate_pay(self):
        return self.salary + self.bonus


class Worker(Employee):

    def __init__(self, name, id, salary, hourly_rate):
        super().__init__(name, id, salary)
        self.hourly_rate = hourly_rate

    def calculate_pay(self):
        return self.salary + self.hourly_rate * 40

