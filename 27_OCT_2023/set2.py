# Set union and intersection

set1 = {11,12,12,14,15,18}
set2 = {13,11, 12, 13, 16, 17}

set3 = set1.union(set2)
print(set3)

set4 = set1.intersection(set2)
print(set4)

set5 = set1.difference(set2)
print(set5)
set6 = set2.difference(set1)
print(set6)