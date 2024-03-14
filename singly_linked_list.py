class Node:
    '''
    Represents a single node in a linked list.

    Attributes:
        value: The value stored in the node.
        next: Reference to the next node in the linked list.
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
    
    def __str__(self):
        '''
        Returns a string representation of the node.

        Returns:
            str: String representation of the node.
        '''
        return f'Node({str(self.value)})'

class LinkedList:
    '''
    Represents a singly linked list data structure.

    Attributes:
        head: The first node in the linked list.
        tail: The last node in the linked list.
        length: The number of nodes in the linked list.
    '''
    def __init__(self, *args):
        '''
        Initializes a new instance of the LinkedList class.

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
                result_string += ' -> '
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
    
    def __getitem__(self, index):
        '''
        Returns the node at the given index.

        Parameters:
            index: The index of the node in the linked list.

        Returns:
            node: The node at the given index.

        Raises:
            IndexError: If the index is out of range.
        '''
        node = self.get(index)
        if node:
            return node
        else:
            raise IndexError("Index out of range")
        
    def __setitem__(self, index, value):
        '''
        Set the value of the node at the given index.

        Parameters:
            index: The index of the node in the linked list.
            value: The value to give the node at the given index.
        
        Raises:
            IndexError: If the index is out of range.
        '''
        node = self.get(index)
        if node:
            node.value = value
        else:
            raise IndexError("Index out of range")
        
    def __iter__(self):
        '''
        Returns an iterator object for iterating over the linked list.

        Returns:
            self: An iterator object.
        '''
        self.current = self.head
        return self

    def __next__(self):
        '''
        Returns the next value in the iteration sequence.

        Raises:
            StopIteration: When the iteration is complete.

        Returns:
            value: The next value in the iteration sequence.
        '''
        if self.current:
            value = self.current.value
            self.current = self.current.next
            return value
        else:
            raise StopIteration
        
    def __len__(self):
        '''
        Returns the length of the linked list.

        Returns:
            int: Length of the linked list.
        '''
        return self.length
    
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
        
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        
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
            node_to_prepend.next = self.head
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
        if index < 0 or index > self.length:
            raise ValueError("Index out of range")

        node_to_insert = Node(value)

        if not self.head:
            self.head = node_to_insert
            self.tail = node_to_insert
        elif index == 0:
            node_to_insert.next = self.head
            self.head = node_to_insert
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            node_to_insert.next = current.next
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
        current = self.head

        if index >= self.length or index < -(self.length):
            raise IndexError("Index out of range")
        
        if index < 0:
            for _ in range(self.length+index):
                current = current.next
        else:
            for _ in range(index):
                current = current.next
        
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

        if node_to_change:
            node_to_change.value = value
        else:
            raise IndexError("Index out of range")
    
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
            self.head = self.head.next
            node_to_pop.next = None
        
        self.length -= 1
        return node_to_pop
    
    def pop(self, index=None):
        '''
        Removes and returns the node at the specified index, or the last node if index is not provided.

        Parameters:
            index (int, optional): The index of the node to remove. If not provided, the last node is removed. Defaults to None.

        Returns:
            node: The removed node.

        Raises:
            IndexError: If the linked list is empty.
            IndexError: If the provided index is out of range.
        '''
        if not self.tail:
            raise IndexError("Cannot pop from an empty linked list")
        
        if index:
            prev_node = self.get(index-1)
            node_to_pop = prev_node.next
            prev_node.next = node_to_pop.next
            node_to_pop.next = None
        else:
            node_to_pop = self.tail
        
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                current = self.head
                while current.next is not self.tail:
                    current = current.next
                
                current.next = None
                self.tail = current
            
        self.length -= 1
        return node_to_pop
    
    def remove(self, value):
        '''
        Removes the first occurrence of a node with the given value from the linked list.

        Parameters:
            value: The value of the node to remove from the linked list.

        Returns:
            node: The removed node.

        Raises:
            ValueError: If the value is not found in the linked list.
        '''
        if not value in self:
            raise ValueError(f"Value {value} not found in the linked list")
        
        index_to_remove = self.find(value)
        node_to_remove = self.get(index_to_remove)
        self.pop(index_to_remove)

        self.length -= 1
        return node_to_remove
    
    def reverse(self):
        '''
        Reverses the order of the nodes in the linked list.
        '''
        current = self.head
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        self.head, self.tail = self.tail, self.head

    def remove_duplicates(self):
        '''
        Removes nodes with duplicate values from the linked list, keeping only the first occurrence of each value.

        Raises:
            RuntimeError: If linked list is empty.
        '''
        if not self.head:
            raise RuntimeError("Cannot remove duplicates from an empty linked list")
        
        seen = set()
        current = self.head
        seen.add(current.value)
        
        while current.next:
            if current.next.value in seen:
                current.next = current.next.next
                self.length -= 1
            else:
                seen.add(current.next.value)
                current = current.next
        
        self.tail = current

    def merge(self, linked_list):
        '''
        Merge another linked list to the end of this linked list.

        Raises:
            TypeError: If argument is not of type LinkedList. 
            RuntimeError: If argument linked list is empty.
        '''
        if not isinstance(linked_list, LinkedList):
            raise TypeError("Argument must be of type LinkedList")
        
        if not linked_list.head:
            raise RuntimeError("The given linked list cannot be empty")

        current = self.head

        while current.next:
            current = current.next
        
        current.next = linked_list.head
        self.tail = linked_list.tail
