# Filter any list with even and odd numbers and create two different lists

input_list = input("Enter your desired numbers with spaces")

user_list = input_list.split()
user_list_even=[]
user_list_odd=[]

# user_list = [int(element) for element in user_list]

# Another alternative solution is -
for i in range(0,len(user_list)):
    user_list[i] = int(user_list[i])

print("List of integers:", user_list)

for i in range(0,len(user_list)):
    if user_list[i] %2 ==0:
        user_list_even.append(user_list[i])
    else:
        user_list_odd.append(user_list[i])

print("The new list with even numbers is : "+str(user_list_even))
print("The new list with odd numbers is : "+str(user_list_odd))


