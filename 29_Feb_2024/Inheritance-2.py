# Hierarchical inheritance
# one parent 2 child


class Father:
    gold = 5

    def home(self):
        print("This is father home")


class S1(Father):
    def home(self):
        print("This is S1 home")

class S2(Father):
    def home(self):
        print("This is S2 home")

Obj1 = S1()
Obj1.home()

#  when the parent and child has the same method and we call child method then the parent method will not be called