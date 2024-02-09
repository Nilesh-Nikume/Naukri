
string = "Great responsibility"  # String
duplicate = []                  # list declare
for i in string:                   #for loop start till end of string
    if string.count(i) > 1:         # check condition single word how many times repeated if it repeated then go to check next condition
        if i not in duplicate:      # check it already in duplicate list or not
            duplicate.append(i)     # if word is not in duplicate it get append in to list
print(duplicate)                    # print list of duplicate

# by using function
# def duplicate_string(string):
#     for i in string:
#         if string.count(i) > 1:
#             if i not in duplicate:
#                 duplicate.append(i)
#     print(duplicate)
#
# string = input("Enter The String: ")
# duplicate = []
# duplicate_string(string)