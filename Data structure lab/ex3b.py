stack = []  # Empty stack

def push(book_title):
    stack.append(book_title)
    print(f'"{book_title}" added to stack.')

def pop():
    if not stack:
        print("Stack is empty! Cannot pop.")
    else:
        print(f'"{stack.pop()}" removed from stack.')

def peek():
    if not stack:
        print("Stack is empty! Nothing to peek.")
    else:
        print(f'Top of stack: "{stack[-1]}"')

def display():
    if not stack:
        print("Stack is empty.")
    else:
        print("Stack contents (top to bottom):")
        for book in reversed(stack):
            print(book)

# Menu
while True:
    print("\n1. Push\n2. Pop\n3. Peek\n4. Display\n5. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        push(input("Enter book title: "))
    elif choice == '2':
        pop()
    elif choice == '3':
        peek()
    elif choice == '4':
        display()
    elif choice == '5':
        break
    else:
        print("Invalid choice!")
