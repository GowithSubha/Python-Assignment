#WAP to implement stack - Push, Pop and Display operations.
def main():
        stack = []
        while True:
            print("1. Push")
            print("2. Pop")
            print("3. Display")
            print("4. Exit")
            # print("5. top of stack")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                element = int(input("Enter element: "))
                stack.append(element)
            elif choice == 2:
                if len(stack) == 0:
                    print("Stack is empty")
                else:
                    print("Popped element is: ", stack.pop())
            elif choice == 3:
                if len(stack) == 0:
                    print("Stack is empty")
                else:
                    print("The stack is: ")
                    for i in range(len(stack) - 1, -1, -1):
                        print(stack[i])
            elif choice == 4:
                break
            # elif choice == 5:
            #     print("The top of stack is: ", stack[-1])
            #     break
            else:
                print("Invalid choice")
                break

if __name__ == "__main__":
    main()

