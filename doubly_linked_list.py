class Node:
    '''
    Represents a single node in a linked list.

    Attributes:
        value: The value stored in the node.
        next: Reference to the next node in the linked list.
        prev: Reference to the previous node in the linked list.
    '''
    def __init__(self, value):
        '''
        Initializes a new instance of the Node class.

        Parameters:
            value: The value to be stored in the node.
        Raises:
            ValueError: If the value is None.
        '''
        if value is None:
            raise ValueError("Node value cannot be None")
        
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        '''
        Returns a string representation of the node.

        Returns:
            str: String representation of the node.
        '''
        return f'Node({str(self.value)})'
    
class DoublyLinkedList:
    '''
    Represents a doubly linked list data structure.

    Attributes:
        head: The first node in the linked list.
        tail: The last node in the linked list.
        length: The number of nodes in the linked list.
    '''
    def __init__(self, *args):
        '''
        Initializes a new instance of the DoublyLinkedList class.

        Parameters:
            *args (optional): Variable number of values or node instances to initialize the linked list.
                If provided, nodes will be created for each value and appended to the linked list in the order they are given.
                If a node instance is provided, it will be appended directly.
                If a raw value is provided, a node will be created for it and appended to the linked list.

        Raises:
            TypeError: If a value cannot be converted to a Node instance.
        '''
        self.head = None
        self.tail = None
        self.length = 0

        for arg in args:
            if isinstance(arg, Node):
                self.append_node(arg)
            else:
                self.append(arg)
            
    
    def __str__(self):
        '''
        Returns a string representation of the linked list.

        Returns:
            str: String representation of the linked list.
        '''
        current_node = self.head
        result_string = ''

        while current_node:
            result_string += str(current_node)
            if current_node.next:
                result_string += ' <=> '
            current_node = current_node.next
        
        return result_string
    
    def __contains__(self, value):
        '''
        Check if the linked list contains the given value.

        Parameters:
            value: The value to search for in the linked list.

        Returns:
            bool: True if the value is found in the linked list, False otherwise.
        '''
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
    
    def append_node(self, node):
        '''
        Appends a node to the end of the linked list.

        Parameters:
            node: The node to append to the linked list.

        Raises:
            TypeError: If the argument is not of type: Node.
        '''
        if not isinstance(node, Node):
            raise TypeError("Invalid node type. Expected Node instance.")
        
        if self.head:
            self.tail.next = node
            node.prev = self.tail
        else:
            self.head = node
        
        self.tail = node
        self.length += 1
    
    def append(self, value):
        '''
        Appends a new node with the given value to the end of the linked list.

        Parameters:
            value: The value to be stored in the new node.
        '''
        node_to_append = Node(value)

        if self.head:
            self.tail.next = node_to_append
            node_to_append.prev = self.tail
        else:
            self.head = node_to_append
        
        self.tail = node_to_append
        self.length += 1

    def prepend(self, value):
        '''
        Prepends a new node with the given value to the beginning of the linked list.

        Parameters:
            value: The value to be stored in the new node.
        '''
        node_to_prepend = Node(value)

        if self.head:
            self.head.prev = node_to_prepend
            node_to_prepend.next = node_to_prepend
        else:
            self.tail = node_to_prepend
        
        self.head = node_to_prepend
        self.length += 1

    def insert(self, index, value):
        '''
        Inserts a new node with the given value to the linked list at the given index.

        Parameters:
            index: The index the new node will be inserted at.
            value: The value to be stored in the new node.
        
        Raises:
            ValueError: If index is out of range.
        '''
        if index < -(self.length+1) or index > self.length:
            raise ValueError("Index out of range")
        
        node_to_insert = Node(value)

        if not self.head:
            self.head = node_to_insert
            self.tail = node_to_insert
        elif index == 0 or index == -(self.length+1):
            node_to_insert.next = self.head
            self.head.prev = node_to_insert
            self.head = node_to_insert
        elif index == self.length:
            self.tail.next = node_to_insert
            node_to_insert.prev = self.tail
            self.tail = node_to_insert
        elif index < 0:
            if abs(index) <= (self.length//2):
                current = self.head
                for _ in range(self.length+index):
                    current = current.next
            else:
                current = self.tail
                for _ in range(abs(index) - 1):
                    current = current.prev
            node_to_insert.next = current.next
            node_to_insert.prev = current
            current.next.prev = node_to_insert
            current.next = node_to_insert
        else:
            if index <= (self.length // 2):
                print("Start from head")
                current = self.head
                for _ in range(index - 1):
                    current = current.next
            else:
                print("Start from tail")
                current = self.tail
                for _ in range(self.length - index):
                    current = current.prev
            node_to_insert.next = current.next
            node_to_insert.prev = current
            current.next.prev = node_to_insert
            current.next = node_to_insert
        self.length += 1

    def find(self, value):
        '''
        Searches for the given value in the linked list and returns the index of the first occurrence.

        Parameters:
            value: The value to search for in the linked list.

        Returns:
            index: The index of the first occurrence of the value. If the value is not found, returns -1.
        '''
        current = self.head
        index = 0

        while current:
            if current.value == value:
                return index
            index += 1
            current = current.next

        return -1

    def get(self, index):
        '''
        Returns the node located at the given index.

        Parameters:
            index: The index of the node in the linked list.

        Returns:
            node: The node located at the given index.

        Raises:
            IndexError: If the index is out of range.
        '''
        if index >= self.length or index < -(self.length):
            raise IndexError("Index out of range")
        
        if index < 0:
            if abs(index) <= (self.length//2):
                current = self.head
                for _ in range(self.length+index):
                    current = current.next
                return current
            else:
                current = self.tail
                for _ in range(abs(index) - 1):
                    current = current.prev
                return current
        else:
            if abs(index) <= (self.length//2):
                current = self.head
                for _ in range(index):
                    current = current.next
                return current
            else:
                current = self.tail
                for _ in range(self.length-index-1):
                    current = current.prev
                return current

    def set_value(self, index, value):
        '''
        Sets the given value to the node located at the given index. 

        Parameters:
            index: The index of the node in the linked list.
            value: The value to give the node.
        
        Raises:
            IndexError: If the index is out of range.
        '''
        node_to_change = self.get(index)

        node_to_change.value = value

    def pop_first(self):
        '''
        Removes first node from the linked list and returns the node.

        Returns:
            node: The removed node which was located at index 0.
        Raises:
            IndexError: If the linked list is empty and there are no nodes to pop.
        '''
        if not self.head:
            raise IndexError("Cannot pop from an empty linked list")
        node_to_pop = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next
            node_to_pop.next = None
        
        self.length -= 1
        return node_to_pop
    