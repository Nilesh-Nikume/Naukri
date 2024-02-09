# n = 4
# for i in range(n):
#     print(" " * (n - i), "*" * (2 * i + 1))
# for i in range(n - 2, -1, -1):
#     print(" " * (n - i), "*" * (2 * i + 1))


def Diamod():
    for i in range(Number):
        print(" " *(Number - i),"*"*(2*i+1))
    for i in range(Number -2, -1, -1):
        print(" " * (Number - i), "*" * (2 * i + 1))
Number =int(input("Enter Hight:"))
Diamod()