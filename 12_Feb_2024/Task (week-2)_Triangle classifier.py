side1 = float(input("Enter length of side 1"))
side2 = float(input("Enter length of side 2"))
side3 = float(input("Enter length of side 3"))

if side1==side2==side3:
    print("Equialteral triangle")
elif side1==side2 or side2==side3 or side1==side2:
    print("Isosceles triangle")
else:
    print("Scalene triangle")

