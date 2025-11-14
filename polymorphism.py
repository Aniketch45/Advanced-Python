#duck typing 
class Rbi:
     def __init__(self,amount,years):
        self.years=years
        self.amount=amount
        
     def rateoi(self):
        roi=0.07
        self.intrest=self.amount*(roi*self.years)
        print("Total amount with Intrest is",self.amount+self.intrest)

class Sbi:
     def __init__(self,amount,years):
        self.years=years
        self.amount=amount
        
     def rateoi(self):
        roi=0.07
        self.intrest=self.amount*(roi*self.years)
        print("Total amount with Intrest is",self.amount+self.intrest)
class Icici:
     def __init__(self,amount,years):
        self.years=years
        self.amount=amount
        
     def rateoi(self):
        roi=0.07
        self.intrest=self.amount*(roi*self.years)
        print("Total amount with Intrest is",self.amount+self.intrest)

class Axis:
    def __init__(self,amount,years):
        self.years=years
        self.amount=amount

    def rateoi(self):
        roi=0.07
        self.intrest=self.amount*(roi*self.years)
        print("Total amount with Intrest is",self.amount+self.intrest)

def method(obj):
    obj.rateoi()

amt=int(input("Enter Amount of Loan : "))
years=int(input("Enter Years : "))
bank=input("Enter bank Name:").lower()

if bank=="rbi":
    i=Rbi(amt,years)
elif bank=="sbi":
    i=Sbi(amt,years)
elif bank=="icici":
    i=Icici(amt,years)
elif bank=="axis":
    i=Axis(amt,years)
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

# class Employee:
#     def __init__(self,name,salpday):
#         self.name=name
#         self.salpday=salpday

#     def __mul__(self,other):
#         return self.salpday*other.days
    
# class Timeshift:
#     def __init__(self,name,days):
#         self.name=name
#         self.days=days

# e=Employee("Amit",800)
# t=Timeshift("Amit",25)
# print(f"{e.name} salary is",e*t)


        

