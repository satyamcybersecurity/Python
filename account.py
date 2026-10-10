"""
Create account class with 2 attributes - balance and account number
create methods for debit, credit and printing the balance
"""

class account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount, "was debited from your account")
        print("total balance =", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "was credited to your account")
        print("total balance =", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = account(10000, 219291)
acc1.debit(8000)
acc1.credit(3718)