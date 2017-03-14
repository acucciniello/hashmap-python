from node import Node
from linkedlist import LinkedList

if __name__ == "__main__":
    node1 = Node(4, 4)
    node2 = Node(5, 2)
    node6 = Node(2, 5)
    linkedlist = LinkedList()

    print "%d words in linked list" % len(linkedlist)
    linkedlist.push(node1)
    linkedlist.push(node2)
    linkedlist.push(node6)
    print "%d values in linked list" % len(linkedlist)
    """
    print 'num buckets: ', len(hashmap._buckets)
    print 'num empty buckets: ', hashmap.get_num_empty_buckets()
    print 'longest bucket: ', hashmap.get_longest_bucket()
    print 'shortest bucket: ', hashmap.get_shortest_bucket()
    print 'val in long bucket `weever`: ', hashmap.get('weever')
    print 'change_len: ', hashmap.change_len
    print 'repr: ', repr(hashmap)
    """