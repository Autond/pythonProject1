# count vowels and consonants in a string



# def count_v_c(str1):
#     for i in str1:
#         if (str1[i] == a or e or i or o or u):
#             print(str1[i])
#         i = i+1
#
# str1 = input("Enter string")
# count_v_c(str1)


def count_vowels_and_consonants(string):
    # Define vowels
    vowels = "aeiouAEIOU"

    # Initialize counters
    vowel_count = 0
    consonant_count = 0

    # Iterate through each character in the string
    for char in string:
        # Check if the character is a letter
        if char.isalpha():
            # Increment vowel count if the character is a vowel
            if char in vowels:
                vowel_count += 1
            # Increment consonant count if the character is a consonant
            else:
                consonant_count += 1

    # Return counts
    return vowel_count, consonant_count

# Input a string from the user
string = input("Enter a string: ")

# Call the function to count vowels and consonants
vowels, consonants = count_vowels_and_consonants(string)

# Print the counts
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)