version = "0.0.1"

class Node:
    def __init__(self,data):
        if not isinstance(data,(int,float)):
            raise TypeError(f"'{type(data).__name__}' isn't compatible with 'Node'")
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.__size = 0
        self.__head = None

    def __repr__(self):
        return f"<'LinkedList' object at {hex(id(self))}>"

    @property
    def size(self):
        return self.__size

    def display(self):
        current = self.__head
        for _ in range(self.__size):
            print(current.data,end = " ")
            current = current.next
        print()

    def append(self,data):
        new_node = Node(data)
        new_node.next = self.__head
        self.__head = new_node
        self.__size += 1

    def insert(self,data,index):
        if not 0 <= index <= self.__size:
            raise IndexError(f"index out of bound! {index} doesn't exist in {0} and {self.__size}")
        new_node = Node(data)
        if index == 0:
            new_node.next = self.__head
            self.__head = new_node
        else:
            current = self.__head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.__size += 1

    def insert_at_last(self,data):
        if self.__head is None:
            raise ValueError("linked list is empty!")
        current = self.__head
        new_node = Node(data)
        for _ in range(self.__size - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.__size += 1

    def remove(self):
        if self.__head is None:
            raise ValueError("linked list is empty!")
        self.__head = self.__head.next
        self.__size -= 1

    def remove_at_index(self,index):
        if not 0 <= index < self.__size:
            raise IndexError("index out of range! {index} doesn't exist in {0} and {self.__size - 1}")
        if self.__head is None:
            raise ValueError("linked list empty!")
        if index == 0:
            self.__head = self.__head.next
        else:
            current = self.__head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.__size -= 1

    def remove_at_end(self):
        if self.__head is None:
            raise ValueError("linked list is empty!")
        current = self.__head
        for _ in range(self.__head - 2):
            current = current.next
        current.next = current.next.next
        self.__size -= 1

    def find_max(self):
        if self.__head is None:
            raise ValueError("linked list is empty!")
        max_value = -float("inf")
        current = self.__head
        for _ in range(self.__size):
            if max_value < current.data:
                max_value = current.data
            current = current.next
        return max_value

    def find_min(self):
        if self.__head is None:
            raise ValueError("linked list is empty!")
        min_value = float("inf")
        current = self.__head
        for _ in range(self.__size):
            if min_value > current.data:
                min_value = current.data
            current = current.next
        return min_value

    def find(self,target):
        if self.__head is None:
            raise ValueError("linked list is empty!")
        indexes = []
        current = self.__head
        for x in range(self.__size):
            if current.data == target:
                indexes.append(x)
            current = current.next
        return indexes

