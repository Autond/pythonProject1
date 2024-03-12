# method overriding- same name in the parent and child
# child always override the parent function
# super means call my parent function



class Animal:

    def __init__(self):
        pass


    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def __init__(self):
        pass

    def sound(self):
        super().sound()  # when you want to use parent class implementation,use super keyword
        print("Dog sound")


# a = Animal()
# a.sound()

d = Dog()
d.sound()

