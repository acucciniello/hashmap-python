class Node(object):
  # a Basic Node for each element in the Hashmap:
  # key - index in the Hashmap
  # data = numeric data of Node
  # next = points to the next element in the Linked List
  def __init__(self, data):
    self.key = None
    self.data = data
    self.next = None
  def __repr__(self):
    if self.key != None:
      return "<Node key: %d data: %d>" % (self.key, self.data)
    else:
        return "<Node key: %s data: %d>" % (self.key, self.data)
