# Write a Python program that takes two lists and returns True if they have at least one common member.
from functools import reduce

list1 = list(input("Enter your desired elements of the 1st list: ").split())
list2 = list(input("Enter your desired elements of the 2nd list: ").split())

print("The 1st list is: " + str(list1))
print("The 2nd list is: " + str(list2))

common_elements = list(set(list1) & set(list2))
# set(list1) & set(list2) creates a set that contains only the common elements of list1 and list2.
# The & operator performs the intersection operation.

if len(common_elements) >= 1:
    print(True)
else:
    print(False)

print("The list of common elements is: " + str(common_elements))

# list3 = list1 + list2
# print(list3)
#
# set1 = set(list3)
# print(set1)
#
# if len(list3) > len(set1):
#     print(True)
# else:
#     print(False)
