import sys
class Piggy():
    def __init__(self,balance=0):
        self.balance=balance 
        
    def deposit(self, amount):
        self.balance=self.balance+amount
        print("\nAfter adding, your updated balance is: ₹"+str(self.balance)) 
    
    
    def withdraw(self,amount):
        if (self.balance< 0) or (amount>self.balance):
            print("Insufficient amount in the account. You will be logged out of your account")
            sys.exit()
        self.balance-=amount
        print("\nAfter withdrawing, balance amount is: ₹"+str(self.balance)) 
    
    def check(self):
        print("\nYour current balance is: ₹"+str(self.balance)) 

print("------------------------------Start-------------------------------------------")
p=Piggy()


while True:
    in1=input("\nStart or End: ").lower() 

    if in1== "start":
        in2=input("Add, Withdraw or Check: ").lower()
        if in2=='add':
            amount=float(input("\nAdd amount: "))
            p.deposit(amount)
        elif in2=='withdraw':
            amount=float(input("\nWithdraw amount: "))
            p.withdraw(amount)
        elif in2=='check':
            p.check()
            print("Thank you for banking with us")
            break
            
    else:
        print("You chose to end the transaction.Thank you for banking with us!")
        break
else:
    print("Choose valid option")
