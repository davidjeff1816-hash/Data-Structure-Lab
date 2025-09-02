class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            print("Dequeued:", self.front.data)
            self.front = self.front.next
            if self.front is None:
                self.rear = None

    def display(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            temp = self.front
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")

q = Queue()

while True:
    print("\n1.Enqueue  2.Dequeue  3.Display  4.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        val = int(input("Enter value: "))
        q.enqueue(val)
    elif ch == 2:
        q.dequeue()
    elif ch == 3:
        q.display()
    elif ch == 4:
        break
    else:
        print("Invalid choice!")

