# Dictionary are set of KEY and VALUES pair
# Syntax a = {"Key":"value"}
# In above examples myDict Fast, Harry, Marks are keys and In a Quick Manner, A Coder, [1,2,3]
# myDict = {
#     "Fast": "In a Quick Manner",
#     "Harry": "A Coder",
#     "Marks": [1, 2, 5],
#     "anotherdict": {'harry': 'Player'} # create New dictionary in old dictionary
# }
#
# print(myDict['Fast'])       # OUTPUT In a Quick Manner
# print(myDict['Harry'])      # OUTPUT A Coder
# myDict['Marks'] = [45, 78]  # We can update values of keys
# print(myDict['Marks'])      # OUTPUT [45, 78]
# print(myDict['anotherdict']['harry'])       # OUTPUT Player

Mydetials = {
    "Name": "Nilesh",
    "LastName": "Nikume",
    "PhoneNumber": "9877454561",
}
print(Mydetials['Name'])
print(Mydetials['LastName'])
Mydetials['PhoneNumber'] = "8669177544" # Here for update values don't use ":" need to use " = "
print(Mydetials['PhoneNumber'])
print(type(Mydetials))

'''
Properties of Dictionary:
1. It is unordered.
2. It is mutable.
3. It is index.
4.Can not contain duplicate keys. Duplicate values overwrite to existing value
'''