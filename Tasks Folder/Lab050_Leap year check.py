# def is_leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False
#
# # Input year from the user
# year = int(input("Enter a year: "))
#
# if is_leap_year(year):
#     print(year, "is a leap year.")
# else:
#     print(year, "is not a leap year.")


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Non leap")

useryear = int(input("Enter year"))

is_leap_year(useryear)

