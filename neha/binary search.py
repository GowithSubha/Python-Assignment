# Write a python program to search an element using Binary search technique.
def binary_search(thislist, a, low, high):

    while low <= high:

        mid = low + (high - low)//2

        if thislist[mid] == a:
            return mid

        elif thislist[mid] < a:
            low = mid + 1

        else:
            high = mid - 1

    return -1


thislist = []
n=int(input("Enter the number of items: "))
print("Enter the items: ")
for i in range(0,n):
    item=int(input())
    thislist.append(item)
a = int(input("Enter the item to be searched: "))

print("The given list is", thislist)


print("Element to be found is ", a)

index = binary_search(thislist, a, 0, len(thislist)-1)

if index != -1:
    print("The Index of the element is " + str(index))
else:
    print("Element Not found")
