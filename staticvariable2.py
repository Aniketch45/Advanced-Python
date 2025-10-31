# Modifiying static variable and deleting
class Test1:
    x=100

    def __init__(self):
        self.x=20
        self.y=20
    
    def show(self):
        print("x : ",Test1.x)
        print("inst x : ",self.x)
        print("y : ",self.y)

s1=Test1()
# s1.show()
s2=Test1()
# del Test1.x   # by using refernce varaible we can't delete static variable use class name
# s2.show()
# Test1.x=200
del s1.x
# s1.x=300
s1.show()




























# class Test:
#     a=10
#     def __init__(self):
#         self.b=900
#         print("Inside constructor using self :",self.a)
#         print("Inside constructor using classname :",Test.a)
#     def m1(self):
#         print("inside method using self :",self.a)
#         print("inside method using classname",Test.a)
    
#     @classmethod
#     def m2(cls):
#         print("Inside class method using cls",cls.a)
#         print("inside class methos using class class name",Test.a)

#     @staticmethod
#     def m3():
#         print("inside static method using class name",Test.a)
        

# t1=Test()
# # t1.m1()
# # t1.m2()
# t1.m3()

# class Bank:
#     roi=0.07
#     def __init__(self,name,accnum,balance):
#         self.name=name
#         self.accnum=accnum
#         self.balance=balance

#     def calroi(self):
#         self.total=self.balance+(self.balance*Bank.roi)
       
#     def showinfo(self):
#         print("Account holder name is :",self.name)
#         print("Account Number is :",self.accnum)
#         print("balance is :",self.balance)
#         print("Total Rate of Intrest is :",self.total)

# for i in range(1,4):
#     namecust=input("Enter Your name : ")
#     accno=int(input("Enter Your Account Number : "))
#     bal=int(input("Enter Your balance : "))

#     b1=Bank(namecust,accno,bal)
#     b1.calroi()
#     b1.showinfo()
#     print("Enter",i+1,"'nd Customer Details")
