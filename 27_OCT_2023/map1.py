# input_nums = input("Enter your numbers with spaces: ")
#
# primary_list = input_nums.split()
# for i in range(len(primary_list)):
#     primary_list[i] = int(primary_list[i])
# print(primary_list)

# Alternative way:

# primary_list = [int(x) for x in input("Enter your numbers with spaces: ").split()]
# print(primary_list)

# Alternative way:

primary_list = list(map(int, input("Enter your desired numbers with spaces: ").split()))


def multiply_by_10(n):
    return n * 10


def square(x):
    return x ** 2


new_list = list(map(multiply_by_10, primary_list))
squared_list = list(map(square, primary_list))

print(new_list)
print(squared_list)


# Filter

def even_number(n):
    if n % 2 == 0:
        return n


even_numbers = list(filter(lambda x: x % 2 == 0, primary_list))
odd_numbers = list(filter(lambda x: x % 2 != 0, primary_list))
even_number_res1 = list(filter(even_number, new_list))
even_number_res2 = list(filter(even_number, squared_list))

print(even_number_res2)
print(even_numbers)
print(odd_numbers)
