
def main():
    matrix1 = []
    matrix2 = []
    for i in range(3):
        matrix1.append([])
        matrix2.append([])
        for j in range(3):
            matrix1[i].append(int(input("Enter element For Matrix 1: ")))
            matrix2[i].append(int(input("Enter element For Matrix 2: ")))
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
    print("The product of the two matrices is: ")
    for i in range(3):
        for j in range(3):
            sum = 0
            for k in range(3):
                sum += matrix1[i][k] * matrix2[k][j]
            print(sum, end=" ")
        print()

if __name__ == "__main__":
    main()