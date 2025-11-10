class D:
    pass

class E:
    pass

class F:
    pass

class A(D,E):
    pass

class C(D,F):
    pass

class B(D,E):
    pass

class A(B,C):
    pass

print("mro of A",A.mro())

'''
mro(A)=A+merge(mro(B),mro(C),XYZ)
        A+merge(BDEO,CDFO,XYZ)
        A+B+merge(DEO,CDFO,XYZ)
        A+B+C+merge(DEO,DFO,XYZ)
        A+B+C+D+merge(EO,FO,XYZ)
        A+B+C+D+E+merge(O,FO,XYZ)
        A+B+C+D+E+F+merge(O,O,XYZ)
        A+B+C+D+E+F+O

'''
# class A:
#     pass

# class B(A):
#     pass

# class C(A):
#     pass

# class D(B,C):
#     pass

# print("mro A:",A.mro())
# print("mro B:",B.mro())
# print("mro C:",C.mro())
# print("mro D:",D.mro())


