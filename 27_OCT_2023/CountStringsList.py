user_input = input("Enter your strings separated by spaces: ")

# Splitting the input string into a list of elements
user_list = user_input.split()

user_list = [element for element in user_list]

length = len(user_list)

if user_list[0] == user_list[length-1] and length>2:
    print(length)

else:
    print("The list is not matching the condition")