#WAP to take an array/list of 10 number and rearrange them in ascending order. 

def main():
    list = []
    for i in range(10):
        list.append(int(input("Enter element: ")))
    print("The list is: ", list)
    for i in range(10):
        for j in range(i+1, 10):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    print("The sorted list is: ", list)

if __name__ == "__main__":
    main()