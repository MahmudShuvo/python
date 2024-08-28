class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account=acc

    def debit(self,amount):
        self.balance -=amount
        print("RS.", amount, "was debited")
        print("total balance=", self.get_bal())
    
    def credit(self,amount):
        self.balance +=amount
        print("RS.", amount, "was credited")
        print("total balance=", self.get_bal())

    def get_bal(self):
        return self.balance

acc1=Account(10000,12345)
acc1.debit(1000)
acc1.credit(500)
print(acc1.balance,"in this account :", acc1.account)
acc1.credit(50000)
print("after inclusion of new month salary",acc1.balance)