from node import Node
class Hashmap(object):

  def __init__(self, length=100):
    self.buckets = [None] * length
    self.length = length

  def hashFunction(self, data, isInsert):
    key = data % self.length + 1
    return key

  def insert(self, node):
    key = self.hashFunction(node.data, True)
    node.key = key
    print key
    if self.buckets[key] is None:
      self.buckets[key] = node
      return node
    else:
      current = self.buckets[key]
      while current.next != None:
        current = current.next
      current.next = node
      return self.buckets[key]

  def __repr__(self):
        return '<Hashmap %r>' % self.buckets