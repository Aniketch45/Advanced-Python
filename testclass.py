# class Test():
#     def add(self):
#         n1=int(input("Enter first Number:"))
#         n2=int(input("Enter second Number:"))
#         print("Addition is",n1+n2)
#     def mul(self):
#          n1=int(input("Enter first Number:"))
#          n2=int(input("Enter second Number:"))
#          print("Multiplication is",n1*n2)

# t1=Test()
# t1.mul()

class Employee:
    def __init__(self,eid,ename,sal,department):
        self.empid=eid
        self.empname=ename
        self.esal=sal
        self.dep=department
    def display(self):
        print(f"Empoloyee name is {self.empname} Id id {self.empid} salary is {self.esal} Department is {self.dep}")


e1=Employee(102,"Aniket",45000,"IT")
e1.display()
