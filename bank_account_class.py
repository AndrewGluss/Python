class BankAccount:

    def __init__(self, balance=0):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount: int):
        self._balance += amount

    def withdraw(self, amount: int):
        if amount > self._balance:
            raise ValueError("На счете недостаточно средств")
        else:
            self._balance -= amount

    def transfer(self, account, amount: int):
        if amount > self._balance:
            raise ValueError("На счете недостаточно средств")
        else:
            self._balance -= amount
            account.deposit(amount)


account = BankAccount()

print(account.get_balance())
account.deposit(100)
print(account.get_balance())
account.withdraw(50)
print(account.get_balance())


account = BankAccount(100)

try:
    account.withdraw(150)
except ValueError as e:
    print(e)


account1 = BankAccount(100)
account2 = BankAccount(200)

account1.transfer(account2, 50)
print(account1.get_balance())
print(account2.get_balance())


account1 = BankAccount(100)
account2 = BankAccount(200)

try:
    account1.transfer(account2, 150)
except ValueError as e:
    print(e)
