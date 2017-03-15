from node import Node
from linkedlist import LinkedList
from hashmap import Hashmap
import unittest

class TestCaseNode(unittest.TestCase):
  def setUp(self):
    self.node = Node(7)

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
  


if __name__ == '__main__':
    unittest.main()