# WAP to take two 3x3 matrix and add them.

def main():
    matrix1 = []
    matrix2 = []
    for i in range(3):
        matrix1.append([])
        matrix2.append([])
        for j in range(3):
            matrix1[i].append(int(input("Enter the element for matrix1: ")))
            matrix2[i].append(int(input("Enter the element for matrix2: ")))
    print("The first matrix is: ")
    for i in range(3):
        for j in range(3):
            print(matrix1[i][j], end=" ")
        print()
    print("The second matrix is: ")
    for i in range(3):
        for j in range(3):
            print(matrix2[i][j], end=" ")
        print()
    print("The sum of the two matrices is: ")
    for i in range(3):
        for j in range(3):
            print(matrix1[i][j] + matrix2[i][j], end=" ")
        print()

if __name__ == "__main__":
    main()
