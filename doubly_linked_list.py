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
        if not value:
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
        self.head = None
        self.tail = None
        self.length = 0

        if args:
            pass
    
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