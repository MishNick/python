class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            dequeued_node = self.head
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
            dequeued_node.next = None
            return dequeued_node.data

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data

    def display(self):
        current = self.head
        if current is None:
            print("Queue is empty")
        else:
            while current is not None:
                print(current.data, end=" ")
                current = current.next
            print()
