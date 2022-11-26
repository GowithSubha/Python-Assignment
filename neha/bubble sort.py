# Write a python program to perform Bubble sort on list.
thislist = []
number = int(input("Please Enter the Total Elements : "))
for i in range(number):
    value = int(input("Please enter the %d Item : " %i))
    thislist.append(value)

for i in range(number -1):
    for j in range(number - i - 1):
        if(thislist[j] > thislist[j + 1]):
             temp = thislist[j]
             thislist[j] = thislist[j + 1]
             thislist[j + 1] = temp

print("The Result in Ascending Order : ", thislist)