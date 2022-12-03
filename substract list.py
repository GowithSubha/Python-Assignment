# Write a python program to subtract a list from another list.

list1 = [10, 11, 12]
list2 = [1, 2, 3]
subtracted = list()
for item1, item2 in zip(list1, list2):
    item = item1 - item2
    subtracted.append(item)
print(subtracted)