'''class Outer:
    def __init__(self):
        print("outer Constructor")
    
    class Inner:
        def __init__(self):
            print("inner constructor")

        def m1(self):
            print("inner Method")
    
    def m2(self):
        print("outer method")

Outer().Inner().m1()

inn=Outer().Inner()
inn.m1()

o1=Outer()
o1.m2()
i1=o1.Inner()
i1.m1()'''

# Nested class ex (creating object of inner class in outer class constructor)
class Person:
    def __init__(self,name,gender,mobno):
        self.name=name
        self.gender=gender
        self.mobno=mobno
        self.d=self.Dateofbirth()
        

    class Dateofbirth:
        def __init__(self):
            self.day=2
            self.month=12
            self.year=2004
            
        def show(self):
            print(f"Date of Birth :{self.day}/{self.month}/{self.year}")
    
    def display(self):
        print("Name Of a person : ",self.name)
        print("Gender is : ",self.gender)
        print("Mobile is : ",self.mobno)
        self.d.show()
       

c1=Person("Aniket","male","9098090980")
# d=c1.Dateofbirth(2,"December",2004)
c1.display()



    
            
        
