# Write a Python Program to Check a Number is a Spy Number.
Number = int(input("Enter the Number to Check Spy Number = "))
Temp = Number
Sum = 0
prod = 1

while Temp > 0:
    lastDigit = Temp % 10
    Sum = Sum + lastDigit
    prod = prod * lastDigit
    Temp = Temp // 10

print("The Sum of the Digits     = %d" %Sum)
print("The Product of the Digits = %d" %prod)

if Sum == prod:
    print("\n%d is Spy Number." %Number)
else:
    print("%d is Not a Spy Number." %Number)