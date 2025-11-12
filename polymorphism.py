#bucket 
class Rbi:
    def rateoi(self,amount,years):
        self.roi=0.07
        self.years=years
        self.amount=amount
        self.intrest=self.amount*(self.roi*self.years)
        print("Total amount with Intrest is",self.amount+self.intrest)
   

class Sbi:
    def rateoi(self,amount,years):
        self.roi=0.07
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
i=Rbi()
i.rateoi(amt,years)

        