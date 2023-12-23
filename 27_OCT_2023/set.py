# Initial Blank set
set1 = set()
print(set1)

set2 = set("Subhasish")
set3= {"Subhasi sh"}
# set2 = set("Subhasish"):
#
# This expression creates a set from the characters of the string "Subhasish."
# The resulting set will contain unique elements from the string, removing any duplicate characters.
# For example, if the string is "Subhasish,"
# the set will only contain the unique characters: {'S', 'u', 'b', 'h', 'a', 's', 'i'}.

# set3 = {"Subhasish"}:
#
# This expression creates a set with a single element, which is the string "Subhasish."
# The resulting set will contain the entire string as a single element: {'Subhasish'}.
# So, the key distinction is that set("Subhasish") breaks down the string into its unique characters
# and creates a set of those characters, while {"Subhasish"} creates a set with the entire
# string as a single element.

print(set2)
print(set3)
# Set does not allow any duplicate values
# set2[1] --> Not possible as Like tuple, set is also immutable and does not allow item assignment
print(len(set2))

set4 = {"Subhasish", "Bumba", "Rimo", "Riya", "Amrita", "Bumba", "Subhasish"}
print(set4)


list1= [11,12,14,11,17,12,15,19,14,18,22,11]
print(len(list1))

# To print unique items, we use set. Here order does not matter
set5 = set(list1)

print(set5)
print(len(set5))

