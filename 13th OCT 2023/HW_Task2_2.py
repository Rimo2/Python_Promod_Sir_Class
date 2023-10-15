# Create a program that takes two numbers as input and prints whether
# the first number is greater than, less than, or equal to the second number.


num1 = int(input('Enter the 1st no:\n'))
num2 = int(input('Enter the 2nd no:\n'))

if num1 > num2:
    print(f'The number {num1} is greater than {num2}')

elif num1 < num2:
    print(f'The number {num2} is greater than {num1}')

else:
    print('Both are same numbers')

###########################################################################

# Input two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Use a ternary operator to compare the two numbers
comparison_result = "greater than" if num1 > num2 else ("less than " if num1 < num2 else "equal to")

# Print the comparison result
print(f"The first number is {comparison_result} the second number.")
