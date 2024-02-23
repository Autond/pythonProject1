# Find a substring in a String.
# need explanation

# def find_sub(string):
#     if substr in string:
#         print("present")
#     else:
#         print("not present")
#
# string = input("Enter string")
# substr = input("Enter sunbtring")
#
# find_sub(string)

def find_substring(main_string, substring):
    # Find the index of the substring in the main string
    index = main_string.find(substring)

    # Check if the substring is found
    if index != -1:
        print("The substring '{}' is found at index {} in the main string.".format(substring, index))
    else:
        print("The substring '{}' is not found in the main string.".format(substring))


# Input the main string and substring from the user
main_string = input("Enter the main string: ")
substring = input("Enter the substring to find: ")

# Call the function to find the substring
find_substring(main_string, substring)
