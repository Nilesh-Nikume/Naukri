# 1.int to float
# x = 5
# y = float(x)
# print(y)
# print(type(y))
#
# # output
# 5.0
# <class 'float'>

#2.float to int
# x = 6.3
# y = int (x)
# print(y)
# print(type(y))
#
# OUTPUT:
# 6
# <class 'int'>

#3.int to string

# x = 6
# y = str (x)
# print(y)
# print(type(y))
#
# # OUTPUT
# 6
# <class 'str'>

#4. STRING TO INT

# x = "2232"
# y = int(x)
# print(y)
# print(type(y))
# # OUTPUT
# 2232
# <class 'int'>

#5. STRING TO FLOAT

# x = "2232"
# y = float(x)
# print(y)
# print(type(y))
#
# OUTPUT:
# 2232.0
# <class 'float'>

#6. FLOAT TO STRING

# x = 22.4
# y = str(x)
# print(y)
# print(type(y))
# OUTPUT:
# 22.4
# <class 'str'>

# Example file for working with classes
class myClass():
    def method1(self):
        print("Guru99")

    def method2(self, someString):
        print("Software Testing:" + someString)


def main():
    # exercise the class methods
    c = myClass()
    c.method1()
    c.method2(" Testing is fun")


if __name__ == "__main__":
    main()
