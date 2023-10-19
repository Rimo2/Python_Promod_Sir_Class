# Input three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Use a ternary operator to find the maximum of the three numbers
max_num = num1 if (num1 > num2 and num1 > num3) \
    else (num2 if num2 > num3
          else num3)

# Calculate the square and cube of the largest number
square = max_num ** 2
cube = max_num ** 3

# Print the results
print(f"The largest number is {max_num}")
print(f"The square of the largest number is {square}")
print(f"The cube of the largest number is {cube}")