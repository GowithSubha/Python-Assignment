# write a program to find max in a list

thislist=[]
n=int(input("Enter the number of items: "))
print("Enter the items: ")
for i in range(0,n):
    item=int(input())
    thislist.append(item)
    
max = thislist[0]
for i in thislist:
    if i > max:
        max = i
        
print("Max of all the items in the list is: ", max)