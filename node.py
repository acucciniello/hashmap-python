# a Basic Node for each element in the LinkedList in a Hashmap stores integers
class Node(object): 
  # key = index in the Hashmap
  # data = numeric data of Node
  # next = points to the next Node object in the Linked List
  def __init__(self, data):
    self.key = None
    self.data = data
    self.next = None

  # Computes the official String representation of Node Objects
  # Since we have not defined __str__ this is used for 
  # informal string Representation as well
  def __repr__(self):
    if self.key != None:
      return "<Node key: %d data: %d>" % (self.key, self.data)
    else:
        return "<Node key: %s data: %d>" % (self.key, self.data)
