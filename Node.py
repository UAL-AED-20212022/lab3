class Node(object):
 # Doubly linked node
 def __init__(self, data=None, next=None, prev=None):
    self.data = data
    self.next = next
    self.prev = prev