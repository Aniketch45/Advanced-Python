class Outer:
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

# inn=Outer().Inner()
# inn.m1()

# o1=Outer()
# o1.m2()
# i1=o1.Inner()
# i1.m1()
