duplicate=[]
thislist=[]
num=int(input("Enter the number of items: "))

print("Enter the items:")
for i in range(num):
    item=int(input())
    thislist.append(item)
    
for i in thislist:
    if thislist.count(i)>1  and duplicate.count(i)==0:
        duplicate.append(i)
        
print("The duplicate items are: ", duplicate)
    