# str = "Neha"
# rev_str = " "
#
# for c in str:
#     rev_str = c + rev_str
#
# print(rev_str)


#using function

# def rs (str):
#     rev_str1 = " "
#     for c in str:
#         rev_str1 = c + rev_str1
#     return rev_str1
#
# result = rs("Pramod")
# print(result)


#Palindrome check
# def reverse_string(str):
#     rev_str = ""
#     for c in str:
#         rev_str = c + rev_str
#     return rev_str
#
# original_str = input("Enter the string")
# original_str = original_str.lower()
# rev_str = reverse_string(original_str)
# print(rev_str)
#
# if original_str == rev_str:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

#Another way

str = "Pramod"
rev_str1 = str[::-1]
print(rev_str1)

