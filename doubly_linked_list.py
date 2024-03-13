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