# Multiply all elements of a list by 10
user_input = input("Enter your integers separated by spaces: ")
multiplier = int(input("Enter your desired multiplier: "))


# Splitting the input string into a list of elements
user_list = user_input.split()
new_list = []


def multiply_with_10(user_list, m):
    for i in range(0, len(user_list)):
        user_list[i] = int(user_list[i]) * m
        new_list.append(user_list[i])
    return new_list


print(multiply_with_10(user_list,multiplier))
