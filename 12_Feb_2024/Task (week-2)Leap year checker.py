year = int(input("Enter year"))
print(year)

if year % 4 == 0: #and year % 400 == 0:
    # if year % 100 == 0:
    print("Leap year")
else:
    print("Non leap year")
