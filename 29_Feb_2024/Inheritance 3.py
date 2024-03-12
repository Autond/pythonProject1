# Multiple inheritance
# multiple parents one child
# mother , father. child
class Father:
    def money(self):
        print("Fath money")

class Mother:
    def money(self):
        print("Moth money")

class child(Father,Mother): # whoever is mentioned in the bracket first ,that persons method will be inherited
        pass                # this is how it is solved by python


obj1 = child()
obj1.money()