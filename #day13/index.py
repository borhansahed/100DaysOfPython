# Strings are immutable
nam = "sahed  is good boy"
header ="full - stack developer"

print(len(nam))

# nam.upper not change our main string. python is create new string and copy my existing string
print(nam.upper())
print(nam.rstrip('!'))
# print(nam.replace("sa","ha"))
print(nam.split())
print(header.capitalize())


# you have to add space number in your center(34) function
print(header.center(34))

# you can count your character with the help of count() function
print(header.count('s'))
print(header.startswith('s'))
print(header.endswith('r'))
print(header.endswith('-', 0,6))


str1 = " he is a honest man "
# python find your character or string . if founded then return first index of string or not founded return -1;
print(str1.find("he"))

# in index() function if founded then return first index or not found then return error
# print(str1.index("he"))

# in isalnum() function
# if your string has A-Z, a-z, 0-9 even you don't use extra space then return true or not found then return false

print(nam.isalnum())