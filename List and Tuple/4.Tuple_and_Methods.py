# Creating a tuple using ()
# t = (1, 2, 4, 5)        # Tuple is immutable and is denoted by ()
# print(t)
# print(type(t))
#
# t1 = () # Empty tuple
# print(t1)
#
# t1 = (1,) # Tuple with Single element
# print(t1)
#
# # Printing the elements of a tuple
# print(t[0])

# Cannot update the values of a tuple
# t[0] = 34 # throws an error TypeError: 'tuple' object does not support item assignment

# # Creating a tuple using ()
t = (1, 2, 4, 5, 4, 1, 5 ,2,1 ,1)

print(t.count(1))  # Return number of 1 in tuple and it 4
print(t.index(5))   # Return index of first occurrence of 5 and it in index 3
