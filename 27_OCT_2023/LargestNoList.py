# Write a Python program to find the largest number in a list.
# Write a Python program to find the smallest number in a list.

user_input = input("Enter your integers separated by spaces: ")

# Splitting the input string into a list of elements
user_list = user_input.split()

# Converting elements to integers
user_list = [int(element) for element in user_list]

# Printing the max no

Max_No = max(user_list)
Min_No = min(user_list)

print("The largest no of the list is: "+str(Max_No))
print("The smallest no of the list is: "+str(Min_No))