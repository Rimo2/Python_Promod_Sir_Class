# Write a Python program to find the factorial of a number.

def factorial_of_n(n):
    if n < 0:
        print("Factorial is not possible")
    else:
        result = 1
        for i in range(1, n + 1):
            result = result * i
        return result


num = int(input("Provide your desired no: "))
print("The factorial of the provided no is : " + str(factorial_of_n(num)))
