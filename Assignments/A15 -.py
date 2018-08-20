#A 15 - Marie Kelling

class AccountP(object):
    def __init__(self, name, account_number, initial_amount):
        self._name = name
        self._no = account_number
        self._balance = initial_amount

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        #r = range(0,_balance)
        if (amount < self._balance):
            self._balance -= amount
        else:
            print("Insufficient Funds!!!")
            print()

    def get_balance(self):
        return self._balance

    def dump(self):
        print ("Dump Account Info")
        print()
        s = '%s, %s, balance: %s\n' % (self._name, self._no, self._balance)
        print (s)
              
# Main
print ("Assignment 15 - written by Marie Kelling")
print()

JohnAccount = AccountP('John Smith', '19371554951', 20000)

JohnAccount.deposit(1000)

JohnAccount.withdraw(4000)

JohnAccount.withdraw(3500)

JohnAccount.dump()


