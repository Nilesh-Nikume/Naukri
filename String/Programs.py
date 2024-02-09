# replace
# Letter = '''Hello <|Name|>
#             Welcome and you can join to us on <|DOJ|>'''
# Name = input("Enter your Name: ")
# DOJ = input("Enter you DOJ: ")
#
# Letter = Letter.replace("<|Name|>", Name)
# Letter = Letter.replace("<|DOJ|>", DOJ)
# print(Letter)
##################################################
# count space
# Letter = '''Hello <|Name|>
#             Welcome and you can join to us on <|DOJ|>'''
# space = print("Total Space are:", Letter.count(" "))

###################################################

# Letter = "Hello  Nilesh, are you!!!  "
# space = Letter.replace("  "," ")
# print(space)
####################################################

# letter = "Dear Harry, This Python course is nice! Thanks!"
# print(letter)
#
# formatted_letter = "Dear Harry,\n\tThis Python course is nice!\nThanks!"
# print(formatted_letter)

########################################################

# Numbers = int(input("Enter the number of fruits: "))
# bucket = []
#
# for i in range(Numbers):
#     fruit_name = input("Enter fruit name: ")
#     bucket.append(fruit_name)
#
# print("List of fruits:", bucket)

##########################################
# Find Duplicates in string
# String = " get well soon mamu"
# bucket = []
# for i in String:
#     if String.count(i) > 1:
#         if i not in bucket:
#             bucket.append(i)
# print(bucket)
#######################

# prg for print revers string

# my_name = "Nilesh"
#
# revers = my_name[::-1]
# print(revers)

########################

# my_Name = " Nilesh"
# revers = " "
#
# for i in my_Name:
#     revers = i + revers
# print(revers)


####
list = [4, 5, 6, 7, 8, 9]
# Output: [9, 8, 7, 6, 5, 4]
rev= list [::-1]
print(rev)
