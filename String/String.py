# Differnt ways to use ofstring
#
# Name = "Nilesh"
# Name1 = 'Nilesh'
# Name2 = '''Twinkle, twinkle, little star
# How I wonder what you are
# Up above the world so high
# Like a diamond in the sky
# Twinkle, twinkle, little star
# How I wonder what you are
# '''
# print(Name)
# print(Name1)
# print(Name2)

# Name = "Nilesh"
# for i, j in enumerate(Name):
#     print(f"Word={j}  at Index={i}")
#
# Name = "Nilesh"
# for index, char in enumerate(Name):
#     print(f"Character: {char}, Index: {index}")

Name2 = '''Twinkle, twinkle, little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle, twinkle, little star
How I wonder what you are
'''

for i in Name2:
    print(i)
print(len(Name2))   # for calculating length of string Name2 which 162 including space
