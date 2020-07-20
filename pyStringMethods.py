temp = "this is the MIX OF small and UPPER CASE string variable sachin sachin"

#Return a copy of the string converted to uppercase.
print(temp.upper())

#Return a copy of the string converted to lowercase.
print(temp.lower())

#Return a copy of the string with only its first character capitalized.
print(temp.capitalize()) 

#Return a titlecased version of the string: words start with uppercase characters, all remaining cased characters are lowercase.
print(temp.title())

#Return a copy of the string with uppercase characters converted to lowercase and vice versa.
print(temp.swapcase())

#Return the lowest index in the string where substring sub is found, 
print(temp.find("small"))

#Return the number of occurrences of substring sub in string
print(temp.count("sachin"))