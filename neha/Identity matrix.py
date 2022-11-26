# Write a python program to check a matrix is Identity matrix or not.


matrix=[]
# Taking input of the 1st matrix
num = int(input("Enter the number of rows for N*N matrix: "))
print("Enter the Matrix Element:")
for i in range(num):
    matrix.append([int(j) for j in input().split()])

# check Diagonal elements are 1 and rest elements are 0
point=0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        # check for diagonals element
        if i == j and matrix[i][j] != 1:
            point=1
            break
        #check for rest elements
        elif i!=j and matrix[i][j]!=0:
            point=1
            break

if point==1:
    print("Given Matrix is not an identity matrix.")
else:
    print("Given Matrix is an identity matrix.")