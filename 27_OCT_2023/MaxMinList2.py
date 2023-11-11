user_input = input("Enter your integers separated by spaces: ")

# Splitting the input string into a list of elements
user_list = user_input.split()

# Converting elements to integers
user_list = [int(element) for element in user_list]
length = len(user_list)

maxNo = user_list[0]
minNo = user_list[0]

for i in range(0,length):
    if maxNo > user_list[i]:
        maxNo = maxNo
    else:
        maxNo = user_list[i]

for i in range(0,length):
    if minNo < user_list[i]:
        minNo = minNo
    else:
        minNo = user_list[i]

print("The smallest number in the list is: : "+str(minNo))
print("The largest number in the list is: "+str(maxNo))