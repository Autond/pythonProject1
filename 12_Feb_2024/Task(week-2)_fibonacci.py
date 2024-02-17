#fibonacci series
a,b = 0,1
while a<10:
    print(a, end="")
    a,b = b,a+b

    # a=0,b=1 (a=0)
    # a=1,b=1 (a=1)
    # a=2,b=4 (a=2)
    # a=4,b=8 (a=4)
