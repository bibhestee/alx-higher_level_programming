#!/usr/bin/python3
"""
    module to create a link list
"""


class Node:

    """
    Node (class):
    Attributes:
    Args:
    Raises:
    """
    def __init__(self, data, next_node=None):
        if type(data) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value
    @next_node.setter
     def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value



class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
          new_node = Node(value)
          if self.__head:
              current = self.__head
              while current.next_node:
                  current  = current.next_node
              current.next_node = Node(value)
          else:
              self.__head = new_node

    def __str__(self):
        current = self.__head
        while current:
            print(current.data)
            current = current.next_node
        return ''
