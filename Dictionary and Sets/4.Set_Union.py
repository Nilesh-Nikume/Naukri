s1 = {1, 2, 4, 5, 3, 6, 7}
s2 = {2, 4, 6, 7}

# print(len(s1)) # length of set which is 7
# print(s1.pop()) # pop method use to remove first element from set
# print(s1) # {2, 3, 4, 5, 6, 7}
# print(s1.pop())
# print(s1) # {3, 4, 5, 6, 7}

# s = s1.union(s2) # print all values from both set but not take duplicates values which is present in both set
# print(s) # {1, 2, 3, 4, 5, 6, 7}
# my_set = {1, 2, 3}
# popped_element = my_set.pop()
# print(popped_element)
# print(my_set)
s = s1.intersection(s2) # only take common values from both set
print(s)    # {2, 4, 6, 7}

