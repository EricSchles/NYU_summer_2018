class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
        
    def __str__(self):
        return repr(self.data)
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        if self.head is None:
            self.head = Node(data, None)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data, None)
    
    def pop(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            data = self.head
            self.head = None
            return data
        else:
            cur = self.head
            prev = cur
            cur = cur.next
            while cur.next:
                cur = cur.next
                prev = prev.next
            data = cur.data
            prev.next = None
            return data
    
linked_list = LinkedList()
for i in range(10):
    linked_list.append(i)
 

elem_exists = True
while elem_exists:
   cur = linked_list.pop()
   print(cur)
   if cur is None:
       elem_exists = False
