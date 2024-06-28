set1 = {"a", "b", "c", 3}
set2 = {1, 2, 3}

#Join Sets

set3 = set1.union(set2)
print(set3)

set3 = set1 | set2
print(set3)

set3 = set1.intersection(set2)
print(set3)

set3 = set1.difference(set2)
print(set3)

set3 = set2-set1
print(set3)

set3 = set1.symmetric_difference(set2)  # or set1 ^ set2
print(set3)
