class Bank(object):


    def __init__(self, name , password,details ,balance):
        self.name=name,
        self.password=password,
        self.details=details,
        self.balance=balance

    def debet(self):
        money=int(input("how much money do you want ."))
        self.balance=self.balance-money

john1 = Bank("John", 1234,"jonathon",10000)
   


john1.debet()   
print("your balance is ",john1.balance)
