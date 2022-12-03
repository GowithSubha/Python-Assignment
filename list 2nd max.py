# Write a python program to find out the 2nd largest number from a list.

thislist=[]
num = int(input("Enter the number of elements in the list: "))
for i in range(1, num + 1):
    ele = int(input("Enter elements: "))
    thislist.append(ele)
    
print("The second largest number is: ", sorted(thislist)[-2])