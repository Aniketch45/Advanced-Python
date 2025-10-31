# class Test:
#     def __init__(self):
#         self.a=49
#         self.b=59
    
#     def add(self):
#         print("Addition is : ",self.a+self.b)

#     def sub(self):
#         print("Substraction is : ",self.a-self.b)

#     def show(self):
#         self.add()
#         self.sub()

# t1=Test()
# t1.show()

class Student:
    def __init__(self,name,m1,m2,m3,m4,m5):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4
        self.m5=m5
        self.per=0
        
    def display(self):
          print("Name of Student is :",self.name)
          self.percentage() # instance method call in other method using self variable
          self.grade()
    
    def percentage(self):
         total=(self.m1+self.m2+self.m3+self.m4+self.m5)
         print("Total is :",total)
         self.per=total/5
         print("Percentage Obtained : ",self.per,"%")

    def grade(self):
        if(self.per>=75):
            print("A+ Grade")
        elif(self.per>=60 and self.per<75):
            print("A Grade")
        elif(self.per>=50 and self.per<60):
            print("B Grade")
        elif(self.per>=40 and self.per<50):
            print("C Grade")
        else:
             print("Fail")

for i in range(1,4):
    name=input("Enter your name : ") 
    m1=int(input("Enter marks of 1st sub :"))
    m2=int(input("Enter marks of 2nd sub :"))
    m3=int(input("Enter marks of 3rd sub :"))
    m4=int(input("Enter marks of 4th sub :"))
    m5=int(input("Enter marks of 5th sub :"))
    s1=Student(name,m1,m2,m3,m4,m5)
    s1.display()

            
       
