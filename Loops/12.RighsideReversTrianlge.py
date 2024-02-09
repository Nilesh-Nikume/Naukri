n = 4
for i in range(n):
    for j in range(i):
        print(" ", end=' ')
    for j in range(i,n):
        print("*",end=' ')
    print()

# by Using fumction

# def RightSideReversTrianlge():
#     for i in range(Number):
#         for j in range(i):
#             print(" ", end=' ')
#         for j in range(i,Number):
#             print("*",end=' ')
#         print()
# Number = int(input("Enter the Hight: "))
# RightSideReversTrianlge()