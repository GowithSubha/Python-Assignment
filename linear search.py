#WAP to perform Linear Search technique. 

def main():
    list = []
    n = int(input("Enter number of elements: "))
    for i in range(n):
        list.append(int(input("Enter element: ")))
    print("The list is: ", list)
    element = int(input("Enter element to search: "))
    for i in range(n):
        if list[i] == element:
            print("Element found at index: ", i)
            break
    else:
        print("Element not found")

if __name__ == "__main__":
    main()
    