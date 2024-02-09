# List slicing
friends = ["Harry", "Tom", "Rohan", "Sam", "Divya", 45]
print(len(friends))     # 6
print(friends[0:4])     # ['Harry', 'Tom', 'Rohan', 'Sam']
print(friends[-4:])     # ['Rohan', 'Sam', 'Divya', 45]
print(type(friends))    # <class 'list'>
print(friends[1:3])     # ['Tom', 'Rohan']
print(friends[4:])      # ['Divya', 45]
print(friends[1:6])     # ['Tom', 'Rohan', 'Sam', 'Divya', 45]
print(friends[1:])      # ['Tom', 'Rohan', 'Sam', 'Divya', 45]