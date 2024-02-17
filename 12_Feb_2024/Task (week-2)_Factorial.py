#factorial
# 5! = 5x4x3x2x1

num = int(input("Enter number"))

if num<0:
    print("Fac not possible")
elif num == 0:
    print("Fac not possible")
else:
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
print("Factorial is",fact)

