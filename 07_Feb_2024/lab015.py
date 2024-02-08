name = "batman"
print(len(name))
print(name[3])
#print((name[6])) #index out of range
print(name[len(name)-1])


#strings are immutable
#cannot be changed

string = "Hello"
string[0] = "p"

print(string)
#TypeError: 'str' object does not support item assignment

