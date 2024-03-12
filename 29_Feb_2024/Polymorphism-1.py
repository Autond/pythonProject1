# polymorphism
# same function different forms
class shape:
    def area(self):
        print("shape area")


class square:

    def area(self):
        print("square area")


class circle:

    def area(self):
        print("circle area")


obc = circle()
obc.area()

obs = square()
obs.area()


