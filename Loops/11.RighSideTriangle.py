# n = 4
# for i in range(n):
#     for j in range(i,n):
#         print(" ", end=' ')
#     for j in range(i+1):
#         print("*", end=' ')
#     print()

# by using function:
def Righsidetrianlge():
    for i in range (Number):
        for j in range (i, Number):
            print(" ", end=' ')
        for j in range (i+1):
            print("*", end=' ')
        print()
Number = int(input("Enter The Number: "))
Righsidetrianlge()