def fact(n):
    if n < 0:
        print("Factorial is not defined for negative numbers")

    elif n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


num = int(input("Provide your desired no: "))
print("The factorial of the provided no is : " + str(fact(num)))
