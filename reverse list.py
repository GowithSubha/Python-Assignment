# Write a program to take a list of numbers and reverse the items 

thislist=[]
revlist=[]
num=int(input("Enter the numbers of items: "))
print("Enter the elements: ")
for i in range(0,num):
    ele=int(input())
    thislist.append(ele)

for i in thislist:
    revlist.insert(0,i)


print("The reversed list is: ", revlist)