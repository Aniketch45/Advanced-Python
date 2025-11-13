#duck typing 
class Rbi:
    def rateoi(self,amount,years):
        self.roi=0.08
        self.years=years
        self.amount=amount
        self.intrest=self.amount*(self.roi*self.years)
        print("Total amount with Intrest is",self.amount+self.intrest)
   
class Sbi:
    def rateoi(self,amount,years):
        self.roi=0.05
        self.years=years
        self.amount=amount
        self.intrest=self.amount*(self.roi*self.years)
        print("Total amount with Intrest is",self.amount+self.intrest)

class Icici:
    def rateoi(self,amount,years):
        self.roi=0.07
        self.years=years
        self.amount=amount
        self.intrest=self.amount*(self.roi*self.years)
        print("Total amount with Intrest is",self.amount+self.intrest)

class Axis:
    def rateoi(self,amount,years):
        self.roi=0.07
        self.years=years
        self.amount=amount
        self.intrest=self.amount*(self.roi*self.years)
        print("Total amount with Intrest is",self.amount+self.intrest)


def method(obj):
    obj.rateoi()

amt=int(input("Enter Amount of Loan : "))
years=int(input("Enter Years : "))
bank=input("Enter bank Name:")


if bank=="rbi":
    i=rateoi(amt,years)
elif bank=="sbi":
    i=rateoi(amt,years)
elif bank=="icici":
    i=method(amt,years)
elif bank=="axis":
    i=method(amt,years)
else:
    print("invalid")

method(i)





  # def call(obj):
    #     if hasattr(obj,'rateoi'):
    #         obj.rateoi()
    #     else:
    #         print("object not have rateoi")

# l1=[Rbi(),Sbi(),Icici(),Axis()]

#  for i in l1:
#     i.rateoi(2000,4)


# while l1:
#     i=l1.pop()
#     i.rateoi(2000,5)

class Employee:
    def __init__(self,name,salpday):
        self.name=name
        self.salpday=salpday

    def __mul__(self,other):
        return self.salpday*other.days
    
class Timeshift:
    def __init__(self,name,days):
        self.name=name
        self.days=days

e=Employee("Amit",800)
t=Timeshift("Amit",25)
print(f"{e.name} salary is",e*t)


        

