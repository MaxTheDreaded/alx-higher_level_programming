#!/usr/bin/python3

"""Defines a class Node"""


class Node:
    """Defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the class
          with the given data and optional next_node.

        Parameters:
            data: The data to be stored in the node.
            next_node: The next node in the linked list (default is None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for the data attribute.
        Returns:
            The value of the data attribute.
        """
        return self._data

    @data.setter
    def data(self, value):
        """
        Setter method for the data attribute.
        Parameters:
            value: The new value for the data attribute.
        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """
        Getter method for the next_node attribute.
        Returns:
            The value of the next_node attribute.
        """
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for the next_node attribute.
        Parameters:
            value: The new value for the next_node attribute.
        Raises:
            TypeError: If the value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


"""Defines a class SinglyLinkedList"""


class SinglyLinkedList:
    """Defines a singly linked list"""
    def __init__(self):
        """Initializes the data of the node"""
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new node with the given value into
          the sorted linked list.
        Parameters:
            value (int): The value to be inserted into the linked list.
        Returns:
            None
        """
        new_node = Node(value)
        if self.head is None or self.head.data >= new_node.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and\
                    current.next_node.data < new_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __repr__(self):
        """
        Returns a string representation of the linked list by traversing
        through the nodes and joining their data with newline characters.
        """
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return '\n'.join(nodes)
