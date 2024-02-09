# 1.len(): Returns the length of the string.
# my_string = "Hello, World!"
# print(len(my_string))  # Output: 13

# # 2. capitalize(): Converts the first character to uppercase
# my_string = "hello, world!"
# print(my_string.capitalize())  # Output: Hello, world!

# # 3. upper() and lower(): Converts all characters to uppercase or lowercase, respectively.
#
# my_string = "HelLo, WoRld!"
#
# print(my_string.upper())  # Output: HELLO, WORLD!
#
# print(my_string.lower())  # Output: hello, world!

#4. title(): Converts the first character of each word to uppercase.

# my_string = "hello world"
#
# print(my_string.title())  # Output: Hello World

# 5. count(substring): Returns the number of occurrences of the specified substring.

# my_string = "Hello, hello, hello!"
#
# print(my_string.count("hello"))  # Output: 2

#6. find(substring) and index(substring): Return the lowest index of the substring.
# find() returns -1 if the substring is not found, while index() raises a ValueError

# my_string = "Hello, World!"
# print(my_string.find("World"))  # Output: 7
# print(my_string.index("World"))  # Output: 7

# 7.replace(old, new): Replaces occurrences of the specified old substring with the new substring.
# my_string = "Hello, World!"
# new_string = my_string.replace("World", "Python")
# print(new_string)  # Output: Hello, Python!

#8. startswith(prefix) and endswith(suffix): Checks if the string starts or ends with the specified prefix or suffix

# my_string = "Hello, World!"
# print(my_string.startswith("Hello"))  # Output: True
# print(my_string.endswith("World"))  # Output: False
# print(my_string.endswith("World!"))  # Output: True

#9. strip(), lstrip(), and rstrip(): Removes leading and trailing whitespaces.
# lstrip() removes leading whitespaces, and rstrip() removes trailing whitespaces

# my_string = "   Hello, World!   "
# print(my_string.strip())    # Output: Hello, World!
# print(my_string.lstrip())   # Output: Hello, World!
# print(my_string.rstrip())   # Output:    Hello, World!

#10. split(separator): Splits the string into a list of substrings based on the specified separator.

my_string = "apple,banana,orange"
fruits = my_string.split(",")
print(fruits)  # Output: ['apple', 'banana', 'orange']