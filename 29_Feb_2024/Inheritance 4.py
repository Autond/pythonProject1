# Hybrid -  mix of hierarchical +multiple


class A:
    def home(self):
        print("from A")

class B(A):
    def home(self):
        print("from B")

class C(A):
    def home(self):
        print("from C")

class D(B,C):
    pass

o1 = D()
o1.home()