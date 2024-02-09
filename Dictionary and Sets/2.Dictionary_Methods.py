Mydetails = {
    "Name": "Nilesh",
    "LastName": "Nikume",
    "Address": "Dhule",
    "PhoneNo.": [987467545756, 8689575445]
}
# print(Mydetails['Name'])
# print(Mydetails['LastName'])
# print(Mydetails['Address'])
# print(Mydetails['PhoneNo.'])
# Mydetails['PhoneNo.'] = [865584942]
# print(Mydetails['PhoneNo.'])


# # Dictionary Methods
# # 1. a.item() = Return list of (keys, values) tuple
# print(
#     Mydetails.items())  # OUTPUT dict_items([('Name', 'Nilesh'), ('LastName', 'Nikume'), ('Address', 'Dhule'), ('PhoneNo.', [987467545756, 8689575445])])
#
# # 2. a.keys() =  Return list of Dictionary keys
# print(Mydetails.keys())  # OUTPUT dict_keys(['Name', 'LastName', 'Address', 'PhoneNo.'])
#
# # 3. a.update() = update Dictionary by suppiled "Keys" : "value" pair
# Mydetails.update({"Country": "India"})
# print(
#     Mydetails)  # OutPut {'Name': 'Nilesh', 'LastName': 'Nikume', 'Address': 'Dhule', 'PhoneNo.': [987467545756, 8689575445], 'Country': 'India'}
#
# # 4. a.get()
# print(Mydetails.get("LastName"))  # OUTPUT Nikume
#
# # 5. a.value() = Return all values of keys
# print(Mydetails.values())  # OUTPUT dict_values(['Nilesh', 'Nikume', 'Dhule', [987467545756, 8689575445], 'India'])


