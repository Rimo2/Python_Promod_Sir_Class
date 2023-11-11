user_input = input("Enter your integers separated by spaces: ")

# Splitting the input string into a list of elements
user_list = user_input.split()

# Converting elements to integers
user_list = [int(element) for element in user_list]

len = len(user_list)
sum = 0
for i in range (0,len):
   sum = sum+user_list[i]
print("The summation of all the elements are: "+str(sum))
