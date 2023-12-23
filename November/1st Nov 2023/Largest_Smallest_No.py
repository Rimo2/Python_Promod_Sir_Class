from functools import reduce

input_nos = list(map(int, input("Enter your desired numbers with spaces: ").split()))
print("The list of provided numbers is : " + str(input_nos))

largest_num = reduce(lambda x, y: x if x > y else y, input_nos)
# Here, the reduce() function is used to iteratively apply the lambda function to pairs of elements in the list,
# finding the maximum value. The lambda function checks
# whether the first element of the pair (x) is greater than the second element (y)
# and returns the larger of the two. This process continues until a single value (the maximum) is obtained.
print("The largest no is: " + str(largest_num))

smallest_num = reduce(lambda x,y: x if x<y else y,input_nos)
print("The smallest no is: " + str(smallest_num))

sorted_nums = sorted(input_nos)
print("The largest no using sort function is: " + str(sorted_nums[-1]))
print("The smallest no using sort function is: " + str(sorted_nums[0]))
