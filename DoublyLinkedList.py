from Node import Node

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def insert_at_end(self, data):
        new_item = Node(data, None, None)
        if self.head is None:
            self.head = new_item
            self.tail = self.head
        else:
            new_item.prev = self.tail
            self.tail.next = new_item
            self.tail = new_item
        self.count += 1
    
    def insert_at_start(self, data):    
        pass
                
    
    def print_foward(self):
        for node in self.iter():
            print(node)

    def print_backward(self): 
        current = self.tail 
        while current != None: 
            print(current.data) 
            current = current.prev

    def iter(self): # Iterate the list
        current = self.head
        while current:
            item_val = current.data
            current = current.next
            yield item_val
    
    def delete_front(self):
        pass
