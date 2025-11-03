class Stud:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def show(self):
        print("Stud Name :",self.name)
        print("Stud Marks : ",self.marks)
    
l=[Stud("Aniket",90),Stud("Viki",80),Stud("Shantanu",95),Stud("Chirag",89)]
# print(l)
for i in l:
    i.show()