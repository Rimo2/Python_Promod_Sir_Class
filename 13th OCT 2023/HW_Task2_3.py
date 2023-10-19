# Use the ternary operator to find the maximum of three numbers entered by the user.
# Develop a Python script that calculates the square and cube of a given number.

# Ternary operator --> value_if_true if condition else value_if_false

num1 = int(input('Enter the 1st no:\n'))
num2 = int(input('Enter the 2nd no:\n'))
num3 = int(input('Enter the 3rd no:\n'))

max_value1 = num1 if num1 > num2 else num2
max_value2 = max_value1 if max_value1 > num3 else num3

print(f'The largest number among these 3 numbers is {max_value2}')

square_maxNo = max_value2 ** 2
cube_maxNo = max_value2 ** 3

print(f'The square of the biggest no is {square_maxNo}')
print(f'The cube of the biggest no is {cube_maxNo}')

###################################################################################

# Another way

# Input three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Use a ternary operator to find the maximum of the three numbers
max_num = num1 if (num1 > num2 and num1 > num3) else (num2 if num2 > num3 else num3)

# Calculate the square and cube of the largest number
square = max_num ** 2
cube = max_num ** 3

# Print the results
print(f"The largest number is {max_num}")
print(f"The square of the largest number is {square}")
print(f"The cube of the largest number is {cube}")

###############################################################

# For 4 numbers

# Input four numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))

# Use a series of ternary operators to find the maximum of the four numbers
max_num = num1 if (num1 > num2 and num1 > num3 and num1 > num4) else (
    num2 if num2 > num3 and num2 > num4 else (
        num3 if num3 > num4 else num4
    )
)

# Calculate the square and cube of the largest number
square = max_num ** 2
cube = max_num ** 3

# Print the results
print(f"The largest number is {max_num}")
print(f"The square of the largest number is {square}")
print(f"The cube of the largest number is {cube}")

# max(*args) --> It can have any no of arguments

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

result = max(num1,num2,num3)

print(f'The largest no is {result}')