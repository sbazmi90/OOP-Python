from bank import *



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bank = Bank("John Doe", "Delta, BC", "122-44-55", "jdoe@mail.com")

    account1 = Account("001", "John Doe", 12280)
    account2 = Account("002", "Jack Doe", 14560)

    print(account1.display_account_details())
    print("\n")
    print(account2.display_account_details())
    print("\n")
    # Add 500 to account 1
    account1.deposit(500)

    # Add 750 to account 2
    account2.deposit(750)

    # Withdraw 235 from account 1
    account1.withdraw(230)

    # Withdraw 540 from account 2
    account2.withdraw(540)

    # check with accounts
    account1.display_account_details()
    print("\n")
    account2.display_account_details()
    print("\n")
    bank.display_bank_details()




