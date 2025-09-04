
#Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * (factorial(n-1))

n=int(input("Enter the number: "))
result = factorial(n)
print(f"The factorial of {n} is: {result}")



#Using the Math Module for Calculations
import math
n=int(input("Enter the number: "))
print("square root:",math.sqrt(n))
print("logarithmic: ",math.log(n))
print("Sine:",math.sin(n))