# Write a Python program to sum all numbers in a list.

user_input = input("Enter your integers separated by spaces: ")

# Splitting the input string into a list of elements
user_list = user_input.split()

# Converting elements to integers
user_list = [int(element) for element in user_list]

sum = sum(user_list)
print(sum)

