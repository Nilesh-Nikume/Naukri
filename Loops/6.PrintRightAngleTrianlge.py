# n = 4
# for i in range(n):
#     for j in range(i+1):
#         print("*", end=' ')
#     print()

def Right_Triangle(Hight):
    for i in range(Hight):
        for j in range(i+1):
            print("*", end=' ')
        print()

Hight = int(input("Enter the of triangle: "))
Right_Triangle(Hight)
