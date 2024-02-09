# Number = int(input("Enter the length of Fibonacci series: "))
Number = 6
fib = [0, 1]  # Initialize the first two numbers in the Fibonacci series

for i in range(2, Number):
    next_number = fib[-1] + fib[-2]
    fib.append(next_number)

print(fib)