class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.End = Node(-1)
        self.head = self.End
        self.tail = self.End
    
    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        self.head.prev = new_node
        self.head = new_node
        new_node.prev = None

    def push_back(self, new_data):
        if self.begin() == self.end():
            self.push_front(new_data)

        else:
            new_node = Node(new_data)
            new_node.prev = self.tail.prev
            self.tail.prev.next = new_node
            new_node.next = self.tail
            self.tail.prev = new_node

    def erase(self, node):
        next_node = node.next

        if node == self.begin():
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None

        else:
            node.next.prev = node.prev
            node.prev.next = node.next
            node.prev = None
            node.next = None

        #return next_node

    def insert(self, node, new_data):
        if node == self.end():
            self.push_back(new_data)

        elif node == self.begin():
            self.push_front(new_data)

        else:
            new_node = Node(new_data)
            new_node.prev= node.prev
            new_node.next = node
            node.prev.next = new_node
            node.prev = new_node

    def begin(self):
        return self.head

    def end(self):
        return self.tail


    
n, m = tuple(map(int, input().split()))
dll_in_str= input()
dll = DoublyLinkedList()

for i in range(n):
    dll.push_back(dll_in_str[i])

it = dll.end()
for _ in range(m):
    command = input()

    if command == "L":
        if it != dll.begin():
            it = it.prev
    elif command == "R":
        if i != dll.end():
            it = it.next
    elif command == "D":
        dll.erase(it)
    else:
        new_data = command.split()[1]
        dll.insert(it, new_data)

it = dll.begin()
while it != dll.end():
    print(it.data, end ="")
    it = it.next