# class Parent:
#     a=10
#     def __init__(self):
#         print("Constructor")
    
#     def show(self):
#         print("inst method")

# class Child(Parent):
#     pass

# c=Child()
# print("static variable",c.a)
# print("static variable",Child.a)
# c.show()


# class Employee:
#     ename="Chirag"

#     def __init__(self):
#         print("This is Constructor")

#     def instmethod(self):
#         print("instance method")
    
#     @classmethod
#     def clsmethod(cls):
#         print("class method")

#     @staticmethod
#     def staticmethod():
#         print("Static method")

# class Hr(Employee):
#     pass

# h=Hr()
# print(h.ename)
# print(Hr.ename)
# h.instmethod()
# h.clsmethod()
# Hr.clsmethod()
# Hr.staticmethod()
# h.staticmethod()


# class Mat:
#     def __init__(self):
#         self.x=40
    
#     def display(self):
#         print("Value of x is : ",self.x)

# class Calc(Mat):
#     def __init__(self):             #constructor overloading happens it calls current or latest use super() for calling parent constructor
#         super().__init__()
#         self.y=58

#     def add(self):
#         print("Addition of x & y is : ",self.x+self.y)

# c=Calc()
# c.display()
# c.add()

# class Mat:
#     def __init__(self,x):
#         self.x=x
    
#     def display(self):
#         print("Value of x is : ",self.x)

# class Calc(Mat):
#     def __init__(self,x,y):            
#         super().__init__(x)
#         self.y=y

#     def add(self):
#         print("Addition of x & y is : ",self.x+self.y)

# c=Calc(10,40)
# c.display()
# c.add()

class Car:
    def __init__(self):
        self.brand="maruti"
        self.modname="suzuki"
        self.ftype="disell"
        self.price=3000000
        self.color="white"

    def carmethod(self):
        print(f"Car Brand is :{self.brand}")
        print(f"Car Model is : {self.modname}")
        print(f"Car Fuel Type is :{self.ftype}")
        print(f"Car Price is :{self.price}")
        print(f"Car Color is :{self.color}")

class Person:
    def __init__(self):
        self.name="Amit"
        self.age=89
        self.mobile=4994949494

    def detail(self):
        print(f"Person Name is:{self.name}")
        print(f"Person age is:{self.age}")
        print(f"Person Mobile number is:{self.mobile}")
        

class Employee(Person):
    def __init__(self):
        super().__init__()
        self.dep="hr"
        self.post="dev"
        self.salary=200000
        self.c=Car()
        

    def show(self):
        print(f"Employee Depatment is :{self.dep},Employee Position is :{self.post},Employee Salary is:{self.salary}")
        self.c.carmethod()
e=Employee()
e.show()
e.detail()