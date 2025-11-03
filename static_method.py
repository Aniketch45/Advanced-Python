class calc:
    count=10
    def __init__(self):
        self.m=100

    @staticmethod
    def add(x,y):
        # print("m",self.m)   #error as it doesn't have self
        print("Addition : ",x+y)
        print("count",calc.count)

# calc.add(10,20)
c1=calc()
c1.add(4,23)