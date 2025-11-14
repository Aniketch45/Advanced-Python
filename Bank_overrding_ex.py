#over-riding
class Bank:
    rate=0.12
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        
    def show(self,amount,years):
        print("Name is : ",self.name)
        print("Age is : ",self.age)
        print("Address is : ",self.address)
        amount+=amount*(years*Sbi.rate)
        print("Loan With intrest is :",amount)

class Rbi(Bank):
    rate=0.07
    def show(self,amount,years):
        print("Name is : ",self.name)
        print("Age is : ",self.age)
        print("Address is : ",self.address)
        amount+=amount*(years*Sbi.rate)
        print("Loan With intrest is :",amount)

class Icici(Bank):
    rate=0.04
    def show(self,amount,years):
        print("Name is : ",self.name)
        print("Age is : ",self.age)
        print("Address is : ",self.address)
        amount+=amount*(years*Sbi.rate)
        print("Loan With intrest is :",amount)

class Sbi(Bank):
    rate=0.08
    def show(self,amount,years):
        print("Name is : ",self.name)
        print("Age is : ",self.age)
        print("Address is : ",self.address)
        amount+=amount*(years*Sbi.rate)
        print("Loan With intrest is :",amount)

name=input("Enter your name :")
age=int(input("Enter your age :"))
address=input("Enter your address :")
amount=float(input("Enter loan Amount :"))
year=int(input("Enter years :"))
bank=input("Enter bank name (rbi,sbi,Icici) :").lower()

if bank=="bank":
    d=Bank(name,age,address)
elif bank=="rbi":
    d=Icici(name,age,address)
elif bank=="sbi":
    d=Sbi(name,age,address)
else:
    print("Invalid choice")

d.show(amount,year)
    

       


        

