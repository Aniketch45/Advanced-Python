# class Employee:
#     def __init__(self,id,name,address,sal=0):
#         self.id=id
#         self.name=name
#         self.address=address
#         self.sal=sal
    
#     def show(self):
#         print("Employee Name is : ",self.name)
#         print("Employee Id is : ",self.id)
#         print("Address : ",self.address)
#         print("salary is : ",self.sal)

# class Fulltime(Employee):
#     def fmethod(self):
#         print("Employee salary is : ",self.sal)

# class Parttime(Employee):
#     hrate=500
#     def __init__(self, id, name, address,hours,sal=0):
#         super().__init__(id, name, address, sal)
#         self.hours=hours

#     def pmethod(self,):
#         self.sal+=self.hours*Parttime.hrate

# class Contract(Employee):
#     def __init__(self,id,name,address,month,sal):
#         super().__init__(id,name,address,sal)
#         self.month=month

#     def cmethod(self):
#         self.sal*=self.month

# ch=input("Enter your type of work : ")
# if ch=="fulltime":
#     f1=Fulltime(101,"Aniket","vaijapur",24000)
#     f1.fmethod()
#     f1.show()
# elif ch=="parttime":
#     p1=Parttime(101,"Aniket","vaijapur",34)
#     p1.pmethod()
#     p1.show()
# elif ch=="contract":
#     c1=Contract(101,"Aniket","vaijapur",12,6000)
#     c1.cmethod()
#     c1.show()
# else:
#     print("Invalid Choice")

'''     
class RBI:
    def __init__(self,name,accountnum):
        self.name=name
        self.accountnum=accountnum
    
    def show(self):
        print("Account Holder Name is :",self.name)

class SBI(RBI):
    def __init__(self, name, accountnum,branch):
        super().__init__(name, accountnum)
        self.branch=branch

    def sbimethod(self):
        pass

class MGB(RBI):
    def __init__(self, name, accountnum,branch):
        super().__init__(name, accountnum)
        self.branch=branch

    def mgbmethod(self):
        pass
'''  

#multiple inhertiance example
class P1:
    def method(self):
        print("parent 1 method ")

class P2:
    def method(self):
        print("parent 2 method")

class Child(P1,P2):
    def __init__(self):
        pass

    # def method(self):
    #     print("Child method")

c1=Child()
c1.method()