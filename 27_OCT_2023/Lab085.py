#Set

set1 = set()
set2 = set("Subhasish")
set3 = {1, 2, 2, 3, 4, 5, 6, 7, 7, 8}
print(set2)
print(set3)

# Print unique items
list1 = [ 6, 7, 8, 8, 9,10, 11, 12, 10, 11]
print(len(list1))

set4 = set(list1)
print(set4)

set5 = set3.union(set4)
set6 = set3.difference(set4)
set7 = set3.intersection(set4)
print(set5)
print(set6)
print(set7)