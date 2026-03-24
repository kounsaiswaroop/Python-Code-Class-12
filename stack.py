stack =[]

def push():
    element = input("Enter element to push: ")
    stack.append(element)
    print(element, "pushed to stack.")

def pop():
    if stack:
        print("Popped element: ",stack.pop())
    else:
        print("Stack is empty!")

def peek():
    if stack:
        print("Top element: ",stack[-1])
    else:
        print("Stack is empty!")

def display():
    if stack:
        print("Stack elements: ", stack[::-1])
    else:
        print("Stack is empty!")

while True:
    print("\nStack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        push()
    elif choice == '2':
        pop()
    elif choice == '3':
        peek()
    elif choice == '4':
        display()
    elif choice == '5':
        print("Program exited.")
        break
    else:
        print("Invalid choice! Please try again.")