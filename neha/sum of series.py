# Write a python program to calculate sum of the series 1^2-2^2+3^2-4^2…. +n^n using Recursion.

def sum_of_series(n):
    if n == 1:
        return 1
    else:
        if (n%2 == 0):
            return -n**2 + sum_of_series(n-1)
        else:
            return n**2 + sum_of_series(n-1)
    
n = int(input("Enter the value of n: "))
print("Sum of the series is: ", sum_of_series(n))