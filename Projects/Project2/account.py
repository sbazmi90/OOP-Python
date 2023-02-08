class Account:

    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.add_transaction("deposit", amount)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.add_transaction("withdraw", amount)
        else:
            return "Insufficient funds"

    def display_account_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder Name: {self.account_holder_name}")
        print(f"Balance: {self.balance}")


    def add_transaction(self, transaction_type, amount):
        self.transactions.append((transaction_type, amount))

