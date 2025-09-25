class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number   # public
        self._account_type = "Savings"         # protected (by convention)
        self.__balance = balance               # private

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Invalid withdraw amount")

    # Getter method to access private balance safely
    def get_balance(self):
        return self.__balance


# -----------------------
# Usage
account = BankAccount("123456789", 1000)

print("Account Number (Public):", account.account_number)   #  Accessible
print("Account Type (Protected):", account._account_type)   #  Accessible, but not recommended

# Access balance (private)
print("Balance (via getter):", account.get_balance())       #  Correct way

# Deposit and withdraw
account.deposit(500)
account.withdraw(200)
print("Final Balance:", account.get_balance())

#  Direct access to private variable gives error
try:
    print(account.__balance)
except AttributeError:
    print("Can't access private balance directly!")
