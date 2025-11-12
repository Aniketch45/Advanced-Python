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

amt=int(input("Enter Amount of Loan : "))
years=int(input("Enter Years : "))
bank=input("Enter Bank Name :")
if bank=="rbi":
    i=Rbi()
    i.rateoi(amt,years)
elif bank=="sbi":
    i=Sbi()
    i.rateoi(amt,years)
elif bank=="icici":
    i=Icici()
    i.rateoi(amt,years)
elif bank=="axis":
    i=Axis()
    i.rateoi(amt,years)
else:
    print("invalid")


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


        