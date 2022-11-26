# Write a Python Program to find Prime Factors of a Number using For Loop.

num = int(input("Enter a number: "))
print("The factors of {} are,".format(num))
for i in range(1,num+1):
    if num % i == 0:
        print(i)