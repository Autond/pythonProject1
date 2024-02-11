#max of 3 nos

num1 = int(input("num1 is"))
num2 = int(input("num2 is"))
num3 = int(input("num3 is"))
#
# print(max(num1,num2,num3))

if num1>num2 and num1>num3:
    print("num1 is greatets",num1)
elif num2>num1 and num2>num3:
    print("num2 is greatest",num2)
else:
    print("num3 is the greatest",num3)
