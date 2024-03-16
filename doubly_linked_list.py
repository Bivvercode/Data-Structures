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
        if index < -(self.length) or index > self.length:
            raise ValueError("Index out of range")
        
        node_to_insert = Node(value)

        if not self.head:
            self.head = node_to_insert
            self.tail = node_to_insert
        elif index == 0:
            node_to_insert.next = self.head
            self.head.prev = node_to_insert
            self.head = node_to_insert
        elif index < 0:
            current = self.head
            for _ in range(self.length+index):
                current = current.next
            node_to_insert.next = current.next
            node_to_insert.prev = current
            current.next = node_to_insert
        else:
            current = self.head
            for _ in range(index-1):
                current = current.next
            node_to_insert.next = current.next
            node_to_insert.prev = current
            current.next = node_to_insert
        self.length += 1
