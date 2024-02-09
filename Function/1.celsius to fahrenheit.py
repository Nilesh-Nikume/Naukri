# (10°C × 9/5) + 32 =F formula

# n = 0
# f = (n * 9/5)+32
# print(f)

def celsiustofahrenheit(celsius):
    Fahrenheit = (celsius * 9 / 5) + 32
    print(f"Temp in Fahrenheit is {Fahrenheit}:")


celsius = int(input("Enter the temp: "))
celsiustofahrenheit(celsius)

def factorial(Number):
    for i in range(1,Number+1):
        fact = fact * i
    print(f"Factorial of {Number}", fact)


fact = 1
Number = int(input("Enter the number: "))
factorial(Number)
