# class Add1:
#     def __init__(self,num):
#         self.num=num
    
#     def __add__(self,other):
#         print(self.num)
#         print(other.num)
#         return self.num+other.num

    
# a1=Add1(23)
# a2=Add1(58)
# print("Additon is",a1+a2)    #a1 pass as self a2 as other

# class Add1:
#     def __init__(self,num):
#         self.num=num
    
#     def __add__(self,other):
#         self.total= self.num+other.num
#         return Add1(self.total)

# a1=Add1(23)
# a2=Add1(58)
# a3=a1+a2
# print(a3.num)

# class Add1:
#     def __init__(self,num):
#         self.num=num
    
#     def __add__(self,other):
#         total= self.num+other.num
#         return Add1(total)

#     def __str__(self):
#         return str(self.num)
    
# a1=Add1(23)
# a2=Add1(58)
# a3=a1+a2
# print(a3)

# class fdiv:
#     def __init__(self,num):
#         self.num=num
    
#     def __sub__(self,other):
#         return self.num-other.num

    
# a1=fdiv(23)
# a2=fdiv(58)
# a3=a1-a2
# print(a3)

# class Hel:
#     def __init__(self,rollno,marks):
#         self.rollno=rollno
#         self.marks=marks

#     def __gt__(self,other):                      #magic method
#         return self.marks>other.marks
    
#     def __le__(self,other):
#         return self.marks<=other.marks
    
#     def __ge__(self,other):
#         return self.marks>=other.marks
    
#     def __eq__(self,other):
#         return self.marks==other.marks
    
#     def __ne__(self,other):
#         return self.marks!=other.marks

    

# h1=Hel(2,9)
# h2=Hel(4,99)
# print(f"{h1.rollno} and {h2.rollno} has Marks greater : ",h1>=h2)
# print(f"{h1.rollno} and {h2.rollno} has Marks less: ",h1<=h2)
# print(f"{h1.rollno} and {h2.rollno} has Marks less: ",h1==h2)
# print(f"{h1.rollno} and {h2.rollno} has Marks less: ",h1!=h2)


class Stud:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def __gt__(self,other):
        return self.marks>other.marks
    
    def __lt__(self,other):
        return self.marks<other.marks
    
    def __eq__(self,other):
        return self.marks==other.marks
    

s1=Stud("Aniket",60)
s2=Stud("Viki",77)
if s1>s2:
    print(f"{s1.name} has More Marks than {s2.name}")
elif s1<s2:
    print(f"{s1.name} has less Marks than {s2.name}")
elif s1==s2:
    print(f"{s1.name} and {s2.name} have equal marks")
else:
    print("invalid")

#adding more than 2 objects

class Book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self,other):
        total=self.pages+other.pages
        return Book(total)
    
    def __str__(self):
        return str(self.pages)
    
b1=Book(45)
b2=Book(32)
b3=Book(300)
b4=b1+b2+b3
print(b4)
        
