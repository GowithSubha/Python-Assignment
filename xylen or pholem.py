# Write a python program to check a number is Xylem or phloem.

num = int(input("Enter a number: "))
temp = num
outersum = 0
innersum = 0

while(temp != 0):
    if (temp == num or temp < 10):
        outersum += temp%10
    else:
        innersum += temp%10
        
    temp = temp//10
    
if (outersum == innersum):
    print("{} is a Xylem number.".format(num))
else:
    print("{} is a Phloem number.".format(num))