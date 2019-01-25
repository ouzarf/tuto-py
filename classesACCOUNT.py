class Account:
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def dump(self):
        s = '%s, %s, balance: %s' % \
            (self.name, self.no, self.balance)
        print s

a1 = Account('John Olsson', '19371554951', 20000)
a2 = Account('Liz Olsson',  '19371564761', 20000)
a1.deposit(1000)
a1.withdraw(4000)
a2.withdraw(10500)
a1.withdraw(3500)
print "a1's balance:", a1.balance
a1.dump()
a2.dump()

a1.no = '19371564764'
a1.balance = 100
a1.dump()

#print a1.get_balance()  # correct way of viewing the balance
a1.no = '19371554955'  # this is a "serious crime"
a1.balance = 1000
a1.dump()

a2.no = '19371564764'
a2.name = 'om ouzarf'
a2.dump()