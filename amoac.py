"""class Student():
    def __init__(self,name,fees):
        self.name=name
        self.fees=fees

    def show(self):
        print("Student Name : ",self.name)
        print("Student Fees :",self.fees)

class Test:
    def modify(self):  # it consider as Static method (no @ annotation but called using Test class name)
        self.fees=self.fees+5000
        self.show()

s1=Student("Aniket",35000)
Test.modify(s1)"""

#by using instance method
class Student():
    def __init__(self,name,fees):
        self.name=name
        self.fees=fees

    def show(self):
        print("Student Name : ",self.name)
        print("Student Fees :",self.fees)

class Test:
    def modify(self,s):
        s.fees=s.fees+5000
        s.show()

s1=Student("Aniket",35000)
# Test.modify(s1)
t1=Test()
t1.modify(s1)


    
    