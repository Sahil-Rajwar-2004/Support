version = "0.0.1"

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self,size):
        self.__size = size
        self.__count = 0
        self.__head = None

    def __repr__(self):
        result = "[ "
        current = self.__head
        while current:
            result += f"{current.data} "
            current = current.next
        result += "]"
        return result

    def is_empty(self):
        return self.__count == 0

    def is_full(self):
        return self.__count == self.__head

    def add(self,data):
        if self.is_full():
            raise ValueError("stack is full")
        if isinstance(data,Node):
            new_node = data
        else:
            new_node = Node(data)
        new_node.next = self.__head
        self.__head = new_node
        self.__count += 1

    def remove(self):
        if self.is_empty():
            raise ValueError("stack is empty!")
        data = self.__head.data
        self.__head = self.__head.next
        return data

    def peek(self):
        if self.is_empty():
            raise ValueError("stack is empty!")
        return self.__head.data

    def show(self):
        current = self.__head
        while current:
            print(current.data,end = " ")
            current = current.next
        print("")

    def size(self):
        return self.__count

