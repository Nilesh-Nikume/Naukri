# 1 inch =2.54 cm
# 10 inch = x

# n = 4
# cm = n * 2.54
# print(cm)

def reverstriangle(hight):
    for i in range(hight):
        for j in range(i,hight):
            print("*", end=' ')
        print()
hight = int(input("Enter hight of triangle: "))
reverstriangle(hight)
