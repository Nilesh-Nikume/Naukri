# Defination set is collection of non repetitive elements
# a = {1, 3, 4, 5, 1}
# print(type(a))  # <class 'set'>
# print(a)        # {1, 3, 4, 5} it remove duplicate

# b = {1, 3, 4, 5, False, "Nilesh"}
# print(b)  # {False, 1, 3, 4, 5, 'Nilesh'}

c = {1, 3, 4, 5, False, "Nilesh", "Nilesh", 3, 1, 5, False}
print(c)  # {False, 1, 3, 4, 5, 'Nilesh'}

# how to create empty set

a = set()
print(type(a))