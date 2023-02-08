from account import Account

class Bank:

    def __init__(self, name, address, phone_number, email):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.list_of_accounts = []

    def create_account(self, account_number, account_holder_name, initial_balance):
        account = Account(account_number, account_holder_name, initial_balance)
        self.list_of_accounts.append(account)

    def get_account(self, account_number):
        for account in self.list_of_accounts:
            if account.account_number == account_number:
                return account
        return None

    def all_account(self):
        return self.list_of_accounts

    def display_bank_details(self):
        print(f"Bank Name: {self.name}")
        print(f"Address {self.address}")
        print(f"Phone number: {self.phone_number}")
        print(f"Email: {self.email}")




