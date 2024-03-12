file = open("TestData.txt","r")
content = file.read()
print(content)
file.close()

# open the file

# Mode-
# 'r' for  reading(default)
# 'w' for writing (creates a new file or truncates an existing one)
# 'a' for appending
# 'b' for binary mode
# '+' for updating (reading and writing)

# Read and Write content
# read a file
# reading rntire content = file_object.read()
# line = file_object.readline() for a single line
# lines = file_object.readlines() for all lines in a list

# close the file