# last in, first out order 

class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self):
        self.top = None
    
    def peek(self):
        return self.top
    
    def push(self, data):
        """add to head of stack"""
        # create variable to store current self.top
        next_node = self.top
        # new variable to store new top
        new_top = Node(data, next_node)
        # update self.top to new top
        self.top = new_top

    def pop(self):
        """removes the head from stack"""
        if self.top is None:
            return None
        removed = self.top
        # change the head to next node
        self.top = self.top.next_node
        return removed