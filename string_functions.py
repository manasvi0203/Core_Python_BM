a = "this is python programming"

# converts lowercase to uppercase
print(a.upper())

# converts uppercase to lowercase
print(a.lower())

# converts into title
print(a.title())

# convert first letter into uppercase
print(a.capitalize())

# to count occurence of a letter/word
print(a.count("p"))

# to replace a string with another string
print(a.replace("python", "c"))

# to check if string starts with a particular substring
print(a.startswith("this"))
print(a.startswith("hello"))

# to check if string ends with a particular substring
print(a.endswith("ng"))
print(a.endswith("yt"))

# to check in string is present anywhere
print("py" in a)
print("hello" in a)

print(a.center(100))

# is my sting made up entirely of alphabets
print(a.isalpha())

# is my string made up entirely of numbers
print(a.isdigit())

# is my string made with a combination of numbers and alphabets
print(a.isalnum())

# is my string made of ascii code
print(a.isascii())

# to check if string is in lowercase
print(a.islower())

# to check if string is in uppercase
print(a.isupper())


