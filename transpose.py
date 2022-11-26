# WAP to take a 3x3 matrix and find the transpose of the matrix.

def main():
    matrix = []
    for i in range(3):
        matrix.append([])
        for j in range(3):
            matrix[i].append(int(input("Enter element: ")))
    print("The matrix is: ")
    for i in range(3):
        for j in range(3):
            print(matrix[i][j], end=" ")
        print()
    print("The transpose of the matrix is: ")
    for i in range(3):
        for j in range(3):
            print(matrix[j][i], end=" ")
        print()

if __name__ == "__main__":
    main()
    