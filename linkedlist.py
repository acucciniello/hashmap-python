from node import Node

# A Linked List of Node Objects
class LinkedList(object):

  # head = pointer to the first Node in the Linked List
  # current = pointer to current Node in list, used when Traversing Linked List
  def __init__(self):
    self.head = None
    self.current = None

  # Returns amount of Node objects in the Linked List
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

  # Adds a Node to the end of a Linked List
  # Returns the Node that was added 
  def push(self, node):
    self.current = self.head
    # Add to front of List if it is Empty
    if self.head is None:
      self.head = node
      return self.head
    else:
      # Iterate through Nodes until reached the end
      while self.current.next != None:
        self.current = self.current.next
      self.current.next = node
    return self.current

  # Returns the length of a Linked List Object
  def __len__(self):
    return self.get_length()

  # Returns informal String representation of a Linked List
  def __str__(self):
    return '<LinkedList: %d nodes>' % self.get_length()

  # Returns formal String represention of Linked List and its Nodes
  def __repr__(self):
    nodes = []
    node = self.head
    while not node is None:
      nodes.append(repr(node))
      node = node.next
    return 'LinkedList: Nodes: %r' % nodes

  # Removes a Node from the Linked List with the given value
  # value = Data of the Node object you would like to remove from the Linked List
  def remove(self, value):
    previous = None
    self.current = self.head
    # Attempted to Remove from Empty Linked List
    if self.current is None:
      return 'Linked List is empty, value of: %d is not here' % value
    else:
      while self.current != None:
        if self.current.data == value:
          # Remove the value from the Linked List
          if len(self) is 1:
            previous = None
            self.current = None
            self.head = None
          else:
            previous.next = self.current.next
            self.current = None
          return 'Node with the value: %d was removed from the LinkedList' % value
        else:
          # Specified Value was not in the Linked List
          previous = self.current
          self.current = self.current.next
      return 'Node is not in LinkedList'

