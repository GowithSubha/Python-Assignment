# Write a program to edit a record stored in ‘employee’.txt file.

import subprocess as sp
import time
program_name = "notepad.exe"
filename = "employee.txt"


file = open(filename, "r")
print(file.read())
file.close()


print("Are you sure you want to edit the file? (y/n)")
ch = input()

if ch == "y":
    sp.Popen([program_name, filename])
    t = int(input("Enter the time in seconds that will take to edit your file: "))
    time.sleep(t)
    file = open(filename, "r")
    print("After edited \n \n",file.read())
    file.close()
else:
    print("File not edited!")
    file = open(filename, "r")
    print(file.read())
    file.close()


# sp.Popen([programname, filename])
