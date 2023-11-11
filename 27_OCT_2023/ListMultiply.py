user_input = input("Enter your integers separated by spaces: ")

# Splitting the input string into a list of elements
user_list = user_input.split()
# his uses the default behavior of split() without specifying any delimiter.
# In this case, it treats consecutive
# whitespace (including spaces, tabs, and newlines) as the delimiter and splits the string accordingly.

# Converting elements to integers
user_list = [int(element) for element in user_list]
length = len(user_list)
mul = 1
for i in range(0,length):
    mul = mul * user_list[i]

print("The result of multiplying all the elements are : "+str(mul))

