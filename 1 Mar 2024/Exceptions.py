
try:
    num1 = int(input("Enter num1"))
    num2= int(input("Enter num2"))
    result = num1/num2
except ValueError as v:
    print(v)

except ZeroDivisionError as z:
    print(z)

else:
    print("result is",result)

finally:
    print("this will be executed anyhow")

