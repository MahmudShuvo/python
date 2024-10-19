class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. Current balance: {self.__balance}"
        return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew {amount}. Current balance: {self.__balance}"
        return "Insufficient funds or invalid withdrawal amount."

    def get_balance(self):
        return self.__balance

# Usage
account = BankAccount("John Doe", 100)
print(account.deposit(50))
print(account.withdraw(30))
print(account.get_balance())
