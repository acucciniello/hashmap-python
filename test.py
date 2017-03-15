from node import Node
from linkedlist import LinkedList
from hashmap import Hashmap
import unittest

class TestCaseNode(unittest.TestCase):
  def setUp(self):
    self.node = Node(7)

  def tearDown(self):
    self.node = None
    del self.node

class TestNodeMethods(TestCaseNode):
  def test_init(self):
    # Check all of nodes attributes
    self.assertEqual(self.node.data, 7)
    self.assertEqual(self.node.key, None)
    self.assertEqual(self.node.next, None)

  def test_repr(self):
    # When Key is None
    reprString = repr(self.node)
    self.assertEqual(reprString, "<Node key: None data: 7>")

    # When Key is  number
    self.node.key = 45
    reprString = repr(self.node)
    self.assertEqual(reprString, "<Node key: 45 data: 7>")

class TestCaseLinkedList(unittest.TestCase):
  def setUp(self):
    self.linkedlist = LinkedList()

  def tearDown(self):
    del self.linkedlist

class TestLinkedListMethods(TestCaseLinkedList):
  def test_init(self):
    # Make Sure that LinkedList.head is None upon init
    self.assertEqual(self.linkedlist.head, None)

  def test_len(self):
    # empty LL returns 0 for length
    self.assertEqual(len(self.linkedlist), 0)

    # List with elements returns correct length
    for i in range(20):
      node = Node(i)
      self.linkedlist.push(node)
    self.assertEqual(len(self.linkedlist), 20)

  def test_push(self):
    # Adds element to an Empty List
    node = Node(3)
    output = self.linkedlist.push(node)
  
    self.assertEqual(repr(output), "<Node key: None data: 3>")

    # Adds element to end of LinkedList with items already
    for i in range(7):
      node = Node(i)
      output = self.linkedlist.push(node)
    self.assertEqual(repr(output), "<Node key: None data: 5>")

  def test_remove(self):
    # Does not remove from an Empty Linked List
    node = Node(10)
    outputEmpty = self.linkedlist.remove(node.data)
    self.assertEqual(outputEmpty, "Linked List is empty, value of: 10 is not here")
    # Does not Remove anything if does not exist in Linked List
    for i in range(10):
      node = Node(i)
      self.linkedlist.push(node)
    outputNotHere = self.linkedlist.remove(11)
    self.assertEqual(outputNotHere,'Node is not in LinkedList')

    # Removes correct element
    outputRemove = self.linkedlist.remove(5)
    self.assertEqual(outputRemove, 'Node with the value: 5 was removed from the LinkedList')

  def test_str(self):
    output = str(self.linkedlist)
    self.assertEqual(output, '<LinkedList: 0 nodes>')

  def test_repr(self):
    output = repr(self.linkedlist)
    self.assertEqual(output, 'LinkedList: Nodes: []')

class TestCaseHashMap(unittest.TestCase):
  def setUp(self):
    self.hashmap = Hashmap()

  def tearDown(self):
    del self.hashmap

class TestHashmapMethods(TestCaseHashMap):
  def test_init(self):
    # Test length with default length
    self.assertEqual(self.hashmap.length, 100)
    # Test length with given length
    del self.hashmap
    self.hashmap = Hashmap(5)
    self.assertEqual(self.hashmap.length, 5)
    # Check that buckets are LinkedList Objects
    self.assertEqual(self.hashmap.buckets[3].head, None)

  def test_hashFunction(self):
    # hashes to correct key
    key = self.hashmap.hashFunction(1079)
    self.assertEqual(key, 80)

  def test_insert(self):
    # places into correct location in Hashmap
    node = Node(576)
    insertOutput = self.hashmap.insert(node)
    self.assertEqual(repr(insertOutput), '<Node key: 77 data: 576>')

  def test_remove(self):
    # does not remove from an empty List at specified key
    removeEmpty = self.hashmap.remove(5)
    self.assertEqual(removeEmpty, "Linked List is empty, value of: 5 is not here")

    # does not remove if it is not in List at specified key
    for i in range(10):
      node = Node(i)
      self.hashmap.insert(node)
    outputNotHere = self.hashmap.remove(505)
    self.assertEqual(outputNotHere,'Node is not in LinkedList')

    # removes node from Linked List at specified key with one element
    outputRemove = self.hashmap.remove(5)
    self.assertEqual(outputRemove, 'Node with the value: 5 was removed from the LinkedList')

    #removes node from Linked List at specified key with multiple elements
    node = Node(205)
    self.hashmap.insert(node)
    node = Node(305)
    self.hashmap.insert(node)
    outputRemove = self.hashmap.remove(305)
    self.assertEqual(outputRemove, 'Node with the value: 305 was removed from the LinkedList')

if __name__ == '__main__':
    unittest.main()