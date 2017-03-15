from node import Node

class LinkedList(object):

  def __init__(self):
    self.head = None
    self.current = None

  def get_length(self):
    length = 0
    if self.head is None:
      return length
    else:
      length = 1
      self.current = self.head
      while self.current.next != None:
        self.current = self.current.next
        length = length + 1
      return length

  def push(self, node):
    self.current = self.head
    if self.head is None:
      self.head = node
      return self.head
    else:
      while self.current.next != None:
        self.current = self.current.next
      self.current.next = node
    return self.current

  def __len__(self):
    return self.get_length()

  def __str__(self):
    return '<LinkedList: %d nodes>' % self.get_length()

  def __repr__(self):
    nodes = []
    node = self.head
    while not node is None:
      nodes.append(repr(node))
      node = node.next
    return 'LinkedList: Nodes: %r' % nodes

  def remove(self, value):
    previous = None
    self.current = self.head
    if self.current is None:
      return 'Linked List is empty, value of: %d is not here' % value
    else:
      while self.current != None:
        if self.current.data == value:
          if len(self) is 1:
            previous = None
            self.current = None
            self.head = None
          else:
            previous.next = self.current.next
            self.current = None
          return 'Node with the value: %d was removed from the LinkedList' % value
        else:
          previous = self.current
          self.current = self.current.next
      return 'Node is not in LinkedList'

