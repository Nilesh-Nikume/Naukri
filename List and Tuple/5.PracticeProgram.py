# Prm to take fruits from user and display tht list
# fruit = int(input("How many fruits you want to stored: "))
# basket = []
# for i in range(fruit):
#     user = input("Enter the Fruit which you want to add: ")
#     basket.append(user)
# print("You added in to your basket\n", basket)


# Number = int(input("How Many student get in enroll exam :"))
# Mark = []
# for i in range(Number):
#     Student = int(input(f"Enter the Marks of {Number} Students MARKS of MATH: "))
#     Mark.append(Student)
# print(f"Marks of all {Number} students ", Mark)
# Mark.sort()
# print(Mark)

# list = [12,56,34,77]
# sum = list[0]+list[1]+list[2]+list[3]
# print(sum)



# a = (1, 1, 2 , 6, 0,0,66,5,2,0)
# print(a.count(0))

#############
# find smallest and gratest number

# Method 01
# def Smallest(Numbers):
#     New_list = []
#     for i in range(Numbers):
#         no = int(input(f"Enter {i} Number: "))
#         New_list.append(no)
#     print("New list is:", New_list)
#
#     if New_list[0] < New_list[1] and New_list[0] < New_list[2]:
#         print("Smallest number is: ", New_list[0])
#
#     elif New_list[1] < New_list[0] and New_list[1] < New_list[2]:
#         print("Smallest number is: ", New_list[1])
#     else:
#         print("Smallest number is: ", New_list[2])
#
#
# Numbers = int(input("How Many Numbers you want to add in list: "))
# Smallest(Numbers)
#


# Numbers = int(input("How Many Numbers you want to add in list: "))
# New_List = []
# for i in range(Numbers):
#     list_is = int(input(f"Enter {i+1} Number: "))
#     New_List.append(list_is)
# print(New_List)
#
# New_List.sort()
# print("sorted list ",New_List)
#
# # print("smallest number from given list is:",New_List[0])
#
# print("Length is ",len(New_List))
#
# # print("Greatest number from given list is:",New_List[len(New_List)-1])

def Sort_Numbers(Numbers):
    New_List =[]
    for i in range(Numbers):
        list_is = int(input(f"Enter {i+1} Number: "))
        New_List.append(list_is)
    print("List before sort:", New_List)
    New_List.sort()
    print("List after Number sort:", New_List)
    print("Smallest Number from given list is:", New_List[0]) # print smallest number for list
    print("Largest Number from given list is:", New_List[len(New_List)-1]) # print largest number
    print("second largest number from list is :", New_List[len(New_List)-2]) # print second largest number

Numbers = int(input("How Many Numbers you want to add in list: "))
Sort_Numbers(Numbers)