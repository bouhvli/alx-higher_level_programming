#!/usr/bin/python3
"""7. Singly linked list
this module has Node class and SinglyLinkedList
"""


class Node:
    """Node class
    Attributes:
        __data (int): the value node holdes.
        __next_node (Node): hold the next node.
    """
    def __init__(self, data, next_node=None):
        self.__data = None
        self.data = data
        self.__next_node = None
        self.next_node = next_node

    @property
    def data(self):
        """getter for __data.
        Returns:
            (int): the value of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """setter for __data.
        Args:
            value (int): the value we want to set __data to.
        Attributes:
            __data (int): the value of the node.
        """
        if (not isinstance(value, int)):
            raise TypeError("data must be an intege")
        self.__data = value

    @property
    def next_node(self):
        """getter for __next_node.
        Returns:
            (Node): the value of the next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter for __next_node.
        Args:
            value (Node): the value we want to set __next_node to.
            __next_node (Node): the value of the node.
        """
        if (value is not None and not isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Node class
    Attributes:
        __head (Node): the head of the list.
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """sorted_insert - insert nodes in orde based on the value of
        __data in an increasing order
        Args:
            value (node): the node we want to insert.
        """
        n_node = Node(value)
        if (self.__head is None):
            self.__head = n_node
        elif (value < self.__head.data):
            n_node.next_node = self.__head
            self.__head = n_node
        else:
            tmp = self.__head
            while (tmp.next_node and tmp.next_node.data < value):
                tmp = tmp.next_node
            n_node.next_node = tmp.next_node
            tmp.next_node = n_node

    def printList(self):
        """printList - as the name says
        Returns:
            (str): the string to print - the \n if it exist if not
                return only the string.
        """
        string = ''
        if self.__head is not None:
            tmp = self.__head
            while (tmp):
                string += str(tmp.data)
                string += '\n'
                tmp = tmp.next_node
        if string.endswith('\n'):
            return string[:-1]
        return string

    def __str__(self):
        return self.printList()
