# Write a Python Program to Remove Given Key from a Dictionary.
myDict = {'name': 'Neha', 'age': 21, 'Batch': '2020-23', 'stream': 'BCA'}
print("Dictionary Items  :  ",  myDict)

key = input("Please enter the key that you want to Delete : ")

if key in myDict.keys():
    del myDict[key]
else:
    print("Given Key is Not present in this Dictionary")
    
print("\nUpdated Dictionary = ", myDict)