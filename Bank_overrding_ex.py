class Bank:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

    def show(self):
        pass


class Rbi(Bank):
    rate=0.09
    def __init__(self,name,age,address,amount,years):
        super().__init__(name,age,address)
        self.amount=amount
        self.years=years
    
    def show(self):
        print(self.name)
        print(self.age)
        print(self.address)
        self.amount+=self.amount*(self.years*Rbi.rate)
        print("Loan With intrest is :",self.amount)
        


class Icici(Bank):
    rate=0.04
    def __init__(self,name,age,address,amount,years):
        super().__init__(name,age,address)
        self.amount=amount
        self.years=years
    
    def show(self):
        print(self.name)
        print(self.age)
        print(self.address)
        self.amount+=self.amount*(self.years*Icici.rate)
        print("Loan With intrest is :",self.amount)

       
class Sbi(Bank):
    rate=0.08
    def __init__(self,name,age,address,amount,years):
        super().__init__(name,age,address)
        self.amount=amount
        self.years=years

    def show(self):
        print(self.name)
        print(self.age)
        print(self.address)
        self.amount+=self.amount*(self.years*Sbi.rate)
        print("Loan With intrest is :",self.amount)

    


name=input("Enter your name :")
age=int(input("Enter your age :"))
address=input("Enter your address :")
amount=int(input("Enter loan Amount :"))
year=int(input("Enter years"))

ban=Sbi(name,age,address,amount,year)
ban.show()
    

       


        

