# WAP to take a 3x3 matrix and check if the matrix is Unique Matrix or not.

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
    for i in range(3):
        for j in range(3):
            if matrix[i][j] != matrix[j][i]:
                print("The matrix is not unit.")
                return
    print("The matrix is unit.")

if __name__ == "__main__":
    main()
    