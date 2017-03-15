from node import Node
from linkedlist import LinkedList

class Hashmap(object):

  def __init__(self, length=100):
    listBuckets = []
    for i in range(100):
      listBuckets.append(LinkedList())
    self.buckets = listBuckets
    self.length = length

  def hashFunction(self, data):
    key = data % self.length + 1
    return key

  def insert(self, node):
    key = self.hashFunction(node.data)
    node.key = key
    pushOutput = self.buckets[key].push(node)
    return pushOutput

  def remove(self, data):
    key = self.hashFunction(data)
    removedOutput = self.buckets[key].remove(data)
    return removedOutput

  def __repr__(self):
        return '<Hashmap %r>' % self.buckets