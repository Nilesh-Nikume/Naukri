# n = 4
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end=' ')
#     for j in range(i):
#         print("*",end=' ')
#     for j in range(i+1):
#         print("*", end=' ')
#     print()


# n=4
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=' ')
#     for j in range(i):
#         print("*",end=' ')
#     for j in range(i+1):
#         print("*",end=' ')
#     print()

# by using function

def HillPattern(Hight):
    for i in range (Hight):
        for j in range(Hight-i-1):
            print("", end=' ')
        for j in range(i+1):
            print("*", end=' ')

        print()

Hight = int(input("Enter the hight: "))
HillPattern(Hight)



