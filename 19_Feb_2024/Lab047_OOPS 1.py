# class ,objects

class Person():
    # Attributes-> Data Members
    name = None
    age = None
    id = None
    phone_no = None

    #Behaviour ->Methods
    def talk(self):
        print("i talk")

    def sleep(self):
        print("I sleep")

    def walk(self):
        print("I walk")


def anotherfun():
    print("This is a fun ,not a method becoz this is outside the class")

# objects = classname()
Ram = Person()
Pramod = Person()

print(Pramod.age)
print(Ram.age)


