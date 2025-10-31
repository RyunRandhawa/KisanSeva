class Stack:

    def push(stack, item):
        stack.append(item)
        print("Item pushed:", item)


    def pop(stack):
        if not stack:
            print("Stack is empty")
        else:
            item = stack.pop()
            print("Popped item:", item)


    def display(stack):
        if not stack:
            print("Stack is empty")
        else:
            print("Stack contents:", stack[::-1])  # Print in reverse order


    if __name__ == "__main__":
        stack = []

        while True:
            print("\nMenu:")
            print("1. Push")
            print("2. Pop")
            print("3. Display")
            print("4. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                item = input("Enter item to push: ")
                push(stack, item)
            elif choice == 2:
                pop(stack)
            elif choice == 3:
                display(stack)
            elif choice == 4:
                break
            else:
                print("Invalid Choice")