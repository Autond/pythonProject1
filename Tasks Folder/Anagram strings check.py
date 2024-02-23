#

# def are_anagrams(str1, str2):
#     # Remove spaces and convert to lowercase
#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()
#
#     # Check if the sorted strings are equal
#     return sorted(str1) == sorted(str2)
#
# # Input two strings from the user
# string1 = input("Enter the first string: ")
# string2 = input("Enter the second string: ")
#
# # Check if the strings are anagrams
# if are_anagrams(string1, string2):
#     print("The strings are anagrams.")
# else:
#     print("The strings are not anagrams.")




def are_anagrams(str1, str2):
     # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

     # Check if the sorted strings are equal
    return sorted(str1) == sorted(str2)

 # Input two strings from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

 # Check if the strings are anagrams
if are_anagrams(string1,string2) == True:
    print("anagrams")
else:
    print("not anagrams")
# if are_anagrams(string1, string2):
#      print("The strings are anagrams.")
# else:
#      print("The strings are not anagrams.")
