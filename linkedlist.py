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
    if self.head is None:
      self.head = node
    else:
      self.current = self.head
      while self.current.next != None:
        self.current = self.current.next
      self.current.next = node
    return

  def __len__(self):
    return self.get_length()

  def __iter__(self):
    return self

  def __next__(self):
    if self.current is None:
      self.current = self.head
      raise StopIteration
    else:
      node = self.current
      self.current = self.current.next
      return (node.key, node.data)

  def __str__(self):
    return '<LinkedList: %d nodes>' % self.get_length()

  def __repr__(self):
    nodes = []
    node = self.head
    while not node is None:
      nodes.append(repr(node))
      node = node.next
    return 'LinkedList: Nodes: %r' % nodes