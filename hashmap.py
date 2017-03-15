from linkedlist import LinkedList

# A Hashmap that uses LinkedLists to handle collisions (chaining)
class Hashmap(object):

  # Creates a List of LinkedList objects with given length and stores length
  # buckets = list of Linked List Objects
  # length = length of the bucket list
  def __init__(self, length=100):
    listBuckets = []
    for i in range(length):
      listBuckets.append(LinkedList())
    self.buckets = listBuckets
    self.length = length

  # Calculates the key to find a location in the Hashmap for a Node
  # data = the data of the Node given for insertion or removal
  # Returns key = location of LinkedList to insert or remove node 
  def hashFunction(self, data):
    key = data % self.length + 1
    return key

  # Places a Node in a Linked List based off the key
  # Gets the key to find out where to place the Node
  # Then adds Node to that LinkedList
  def insert(self, node):
    key = self.hashFunction(node.data)
    node.key = key
    pushOutput = self.buckets[key].push(node)
    return pushOutput

  # Removes a Node in the Hashmap 
  # Finds the key to the location of the Node
  # Then iterates through the Linked List until
  # it finds correct Node to remove
  def remove(self, data):
    key = self.hashFunction(data)
    removedOutput = self.buckets[key].remove(data)
    return removedOutput

  # Formal String representation of a Hashmap
  def __repr__(self):
        return '<Hashmap %r>' % self.buckets