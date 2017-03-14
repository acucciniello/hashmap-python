from node import Node
from linkedlist import LinkedList
from hashmap import Hashmap

linkedlist = LinkedList()
node1 = Node(3)
node2 = Node(103)
hashmap = Hashmap()
output = hashmap.insert(node1)
hashmap.insert(node2)
hashmap.insert(Node(455))
print hashmap.buckets[4].next.next
print hashmap
