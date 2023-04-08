class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # add to end of list
    def enqueue(self, data):
        if self.tail is None and self.head is None:
            # head & tail pointing to same node
            self.tail = self.head = Node(data, None)
            return
        
        # add to back of queue, add to next node
        self.tail.next_node = Node(data, None)
        # make the tail the next node
        self.tail = self.tail.next_node
        return
    
    # remove head from list
    def dequeue(self):
        if self.head is None:
            return None
        # store current head in new variable
        removed = self.head
        # shift to next node
        self.head = self.head.next_node
        # move head & tail to None if empty
        if self.head is None:
            self.tail = None
        return removed