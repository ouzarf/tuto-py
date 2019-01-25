class Account:
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def dump(self):
        s = '%s, %s, balance: %s' % \
            (self.name, self.no, self.balance)
        print s


print
a1 = Account('John Olsson', '19371554951', 20000)
a1.deposit(1000)
a1.withdraw(4000)
a1.withdraw(3500)
a1.dump()
print
print a1.balance       # it works, but a convention is broken
print a1.get_balance()  # correct way of viewing the balance
print

a1.name = 'ouzarf Med'  # this is a "serious crime"
a1.balance = 1000
a1.dump()

