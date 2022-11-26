thislist=[]
num=int(input("Enter the number of items: "))
print("Enter the items: ")
for i in range(0,num):
    ele=int(input())
    thislist.append(ele)
    
sum = 0
for i in thislist:
    sum += i
    
print("Sum of all the items in the list is: ", sum)