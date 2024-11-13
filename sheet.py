1 _ STACK 

class Stack:
    def __init__(self, max_size: int):
        """Initialize a stack with a maximum size."""
        self.stack = []
        self.max_size = max_size

    def push(self, value: int) -> None:
        """Push a value onto the stack if there is space."""
        if self.size() >= self.max_size:
            print(f"Stack Overflow: Cannot push {value}, stack is full.")
        else:
            self.stack.append(value)

    def pop(self) -> int | None:
        """Pop the top value from the stack if not empty."""
        if self.is_empty():
            print("Stack Underflow: Cannot pop from an empty stack.")
            return None
        return self.stack.pop()

    def peek(self) -> int | str:
        """Return the top value of the stack without removing it."""
        if self.is_empty():
            return "Stack is empty."
        return self.stack[-1]

    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return not self.stack

    def size(self) -> int:
        """Return the current size of the stack."""
        return len(self.stack)

# Test the Stack implementation
if __name__ == "__main__":
    stack = Stack(max_size=3)
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)  # Should trigger stack overflow

    print(stack.pop())  # Outputs 30
    print(stack.pop())  # Outputs 20
    print(stack.pop())  # Outputs 10
    print(stack.pop())  # Should trigger stack underflow

2 _ INFIX_POSTFIX

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    stack = []

    def greater_precedence(op1, op2):
        return precedence[op1] > precedence[op2]

    for char in expression:
        if char.isalnum():  # Operand
            output.append(char)
        elif char == '(':  # Opening parenthesis
            stack.append(char)
        elif char == ')':  # Closing parenthesis
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Pop '('
        else:  # Operator
            while (stack and stack[-1] != '(' and
                   (greater_precedence(stack[-1], char) or
                    (precedence[stack[-1]] == precedence[char] and char != '^'))):
                output.append(stack.pop())
            stack.append(char)

    # Pop all remaining operators in the stack
    while stack:
        output.append(stack.pop())

    return ''.join(output)


# Test the function
expression = "a+b*(c^d-e)^(f+g*h)-i"
postfix = infix_to_postfix(expression)
print("Infix: ", expression)
print("Postfix: ", postfix)

3 _ LINEAR _ QUEUE

size = int(input("Enter the size of queue: "))
queue = [None] * size
front = -1
rear = -1

def enqueue(element):
    global rear, front
    if rear == size - 1:  # Check if the queue is full
        print("Overflow: The queue is full.")
    else:
        if front == -1:  # If the queue is initially empty
            front = 0
        rear += 1
        queue[rear] = element
        print(f"Element {element} enqueued to queue.")
        print(f"Current queue: {queue[front:rear+1]}")

def dequeue():
    global rear, front
    if front == -1:  # Check if the queue is empty
        print("Underflow: The queue is empty.")
    else:
        dequeued_element = queue[front]
        queue[front] = None  # Optional: Clear the element
        if front == rear:  # Queue becomes empty after this operation
            front = rear = -1
        else:
            front += 1
        print(f"Element {dequeued_element} dequeued from queue.")
        print(f"Current queue: {queue[front:rear+1]}")

# Menu for performing queue operations
while True:
    action = int(input("Enter '1' to add element, '2' to remove element, or '3' to exit: "))
    if action == 1:
        data = int(input("Enter the element: "))
        enqueue(data)
    elif action == 2:
        dequeue()
    elif action == 3:
        print("Exiting...")
        break
    else:
        print("Invalid action. Please enter '1', '2', or '3'.")

4 _ CIRCULAR QUEUE 

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = 0

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:  # Check if the queue is full
            print("Circular Queue is full, cannot enqueue more items.")
        else:
            self.queue[self.rear] = item
            self.rear = (self.rear + 1) % self.size

    def dequeue(self):
        if self.front == self.rear:  # Check if the queue is empty
            print("Circular Queue is empty, cannot dequeue more items.")
            return None
        else:
            item = self.queue[self.front]
            self.queue[self.front] = None  # Optional: Clear the dequeued position
            self.front = (self.front + 1) % self.size
            return item

    def display(self):
        if self.front == self.rear:  # Check if the queue is empty
            print("Circular Queue is empty.")
        else:
            print("Queue elements: ", end="")
            i = self.front
            while i != self.rear:
                print(self.queue[i], end=" ")
                i = (i + 1) % self.size
            print()


# Testing the CircularQueue
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
print("Queue after enqueue: ", end="")
cq.display()

print("Dequeue item: ", cq.dequeue())
print("Queue after dequeue: ", end="")
cq.display()

cq.enqueue(40)
print("Queue after enqueue: ", end="")
cq.display()

5 _ LINKED LIST 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at the beginning.")

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            print(f"Inserted {data} at position {position}.")
            return
        temp = self.head
        for _ in range(position - 2):
            if temp is None:
                print(f"Position {position} is out of bounds.")
                return
            temp = temp.next
        if temp is None:
            print(f"Position {position} is out of bounds.")
        else:
            new_node.next = temp.next
            temp.next = new_node
            print(f"Inserted {data} at position {position}.")

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"Inserted {data} at the end (list was empty).")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        print(f"Inserted {data} at the end.")

    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        self.head = self.head.next
        temp = None
        print("Deleted element at the beginning.")

    def delete_at_end(self):
        if self.head is None:
            print("List is empty.")
            return
        if self.head.next is None:
            self.head = None
            print("Deleted element at the end.")
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
        print("Deleted element at the end.")

    def delete_element(self, data):
        temp = self.head
        if temp is not None:
            if temp.data == data:
                self.head = temp.next
                temp = None
                print(f"Deleted element {data}.")
                return
        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            print(f"Element {data} not found in the list.")
            return
        prev.next = temp.next
        temp = None
        print(f"Deleted element {data}.")

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Test the LinkedList class
ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_beginning(20)
ll.insert_at_position(30, 2)
ll.insert_at_position(40, 4)
ll.insert_at_end(50)
ll.print_list()

ll.delete_at_beginning()
ll.print_list()

ll.delete_at_end()
ll.print_list()

ll.delete_element(30)
ll.print_list()

ll.delete_element(100)
ll.print_list()


6 _ DOUBLY LL

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        print(f"Inserted {data} at the beginning.")

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 1:
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
            print(f"Inserted {data} at position {position}.")
            return
        temp = self.head
        for _ in range(position - 2):
            if temp is None:
                print(f"Position {position} is out of bounds.")
                return
            temp = temp.next
        if temp is None:
            print(f"Position {position} is out of bounds.")
        else:
            new_node.next = temp.next
            if temp.next is not None:
                temp.next.prev = new_node
            temp.next = new_node
            new_node.prev = temp
            print(f"Inserted {data} at position {position}.")

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"Inserted {data} at the end (list was empty).")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        print(f"Inserted {data} at the end.")

    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        temp = None
        print("Deleted element at the beginning.")

    def delete_at_end(self):
        if self.head is None:
            print("List is empty.")
            return
        if self.head.next is None:
            self.head = None
            print("Deleted element at the end.")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.prev.next = None
        temp = None
        print("Deleted element at the end.")

    def delete_element(self, data):
        temp = self.head
        if temp is not None and temp.data == data:
            self.head = temp.next
            if self.head is not None:
                self.head.prev = None
            temp = None
            print(f"Deleted element {data}.")
            return
        while temp is not None and temp.data != data:
            temp = temp.next
        if temp is None:
            print(f"Element {data} not found in the list.")
            return
        if temp.next is not None:
            temp.next.prev = temp.prev
        if temp.prev is not None:
            temp.prev.next = temp.next
        temp = None
        print(f"Deleted element {data}.")

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


# Testing the DoublyLinkedList class
d = DoublyLinkedList()
d.insert_at_end(10)
d.insert_at_beginning(20)
d.insert_at_position(30, 2)
d.insert_at_position(40, 4)
d.insert_at_end(50)
d.print_list()

d.delete_at_beginning()
d.print_list()

d.delete_at_end()
d.print_list()

d.delete_element(30)
d.print_list()

d.delete_element(100)
d.print_list()


7 _ LINKWD STACK _ QUEUE 

class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


class LinkedStack:
    def __init__(self, max_size):
        self.top = None
        self.size = 0
        self.max_size = max_size

    def push(self, item):
        if self.size >= self.max_size:
            print("Stack is full (overflow)")
            return
        temp = Node(item)
        temp.link = self.top
        self.top = temp
        self.size += 1

    def pop(self):
        if self.top is None:
            print("Stack is empty (underflow)")
            return None
        else:
            temp = self.top
            item = temp.data
            self.top = self.top.link
            self.size -= 1
            del temp
            return item

    def peek(self):
        if self.top is None:
            print("Stack is empty (underflow)")
            return None
        return self.top.data

    def print_s(self):
        if self.top is None:
            print("Stack is empty")
        else:
            temp = self.top
            print("Stack content:", end=" ")
            while temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.link
            print("None")


class LinkedQueue:
    def __init__(self, max_size):
        self.front = self.rear = None
        self.size = 0
        self.max_size = max_size

    def enq(self, item):
        if self.size >= self.max_size:
            print("Queue is full (overflow)")
            return
        temp = Node(item)
        if self.rear is None:
            self.front = self.rear = temp
        else:
            self.rear.link = temp
            self.rear = temp
        self.size += 1

    def deq(self):
        if self.front is None:
            print("Queue is empty (underflow)")
            return None
        else:
            temp = self.front
            item = temp.data
            self.front = self.front.link
            self.size -= 1
            if self.front is None:
                self.rear = None
            del temp
            return item

    def print_q(self):
        if self.front is None:
            print("Queue is empty")
        else:
            temp = self.front
            print("Queue content:", end=" ")
            while temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.link
            print("None")


# Test LinkedStack and LinkedQueue
print("Stack:")
s = LinkedStack(max_size=3)
s.pop()
s.push(10)
s.print_s()
s.push(20)
s.print_s()
s.push(30)
s.print_s()
print("Top element:", s.peek())
s.pop()
s.print_s()

print("\nQueue:")
q = LinkedQueue(max_size=3)
q.deq()
q.enq(1)
q.print_q()
q.enq(2)
q.print_q()
q.enq(3)
q.print_q()
q.deq()
q.print_q()


8 _ LINEAR _ BINARY _ SEARCH 

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Main program
arr = [10, 2, 32, 45, 5, 65, 78, 9]

while True:
    print("\nChoose the search method:")
    print("1. Linear Search")
    print("2. Binary Search")
    print("3. Exit")
    
    choice = int(input("Enter 1, 2, or 3: "))
    
    if choice == 1:
        print("Original array:", arr)
    elif choice == 2:
        sorted_arr = sorted(arr)
        print("Sorted array:", sorted_arr)
    elif choice == 3:
        print("Exiting the program...")
        break
    else:
        print("Invalid choice")
        continue
    
    target = int(input("Enter the value to search: "))
    
    if choice == 1:
        result = linear_search(arr, target)
    elif choice == 2:
        result = binary_search(sorted_arr, target)
    
    if result != -1:
        print(f"Value found at index {result}")
    else:
        print("Value not found in the list")


9 _ QUICK SORT 

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    array = [3, 6, 8, 10, 1, 2, 1]
    sorted_array = quick_sort(array)
    print("Original array:", array)
    print("Sorted array:", sorted_array)


9 _ MERGE SORT 

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array

if __name__ == "__main__":
    array = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", array)
    sorted_array = merge_sort(array)
    print("Sorted array:", sorted_array)


10 _ BST 

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")


def levelorder(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while queue:
        node = queue.pop(0)
        print(node.val, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# Main program
root = None
root = insert(root, 50)
root = insert(root, 25)
root = insert(root, 30)
root = insert(root, 80)
root = insert(root, 75)
root = insert(root, 10)
root = insert(root, 98)

print("BST with values 50, 25, 30, 80, 75, 10, and 98:")

print("Inorder Traversal:")
inorder(root)

print("\nPreorder Traversal:")
preorder(root)

print("\nPostorder Traversal:")
postorder(root)

print("\nLevel Order Traversal:")
levelorder(root)










