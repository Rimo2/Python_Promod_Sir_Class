# Filter any list with even and odd numbers and create two different lists using function

user_input = input("Provide your desired numbers with spaces: ")
user_list = user_input.split(" ")

for i in range(len(user_list)):
    user_list[i] = int(user_list[i])
print("The provided list is: " + str(user_list))


def pos_num(n):
    if n > 0:
        return n


def even_no(n):
    return n % 2 == 0


def odd_no(n):
    return n % 2 != 0


a = list (filter(even_no, user_list))
b = list (filter(odd_no, user_list))

print(a)
print(b)
