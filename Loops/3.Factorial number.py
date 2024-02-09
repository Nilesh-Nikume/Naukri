# n! = 1 X 2 X 3 X ..... X n
# 5! = 1 X 2 X 3 X 4 X 5

# Factorial = 1
# Number = int(input("Which Number you want factorial: "))
# for i in range(1,Number+1):
#     Factorial = Factorial * i
# print(Factorial)
#

#by using function
def fact():
    Factorial = 1
    for i in range(1, Number+1):
        Factorial = Factorial * i
    print(Factorial)

Number = int(input("Enter the the number: "))
fact ()