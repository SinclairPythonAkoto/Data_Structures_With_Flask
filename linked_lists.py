class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

# the node can now be used as..
# node2 = Node()
# node1 = Node("data", node2)


class LinkedList:
    """wrapper to keep of head of linkedlist"""
    def __init__(self):
        self.head = None
        self.last_node = None
    
    def print_linkedlist(self):
        ll_string = ""
        node = self.head
        if node is node:
            print(None)
        while node:
            # convert each node.data to string & concatenate 
            ll_string += f" {str(node.data)} ->"
            # switch to next node after looping 
            node = node.next_node
        # add None to end of node
        ll_string += " None"
        print(ll_string)

    def insert_beginning(self, data):
        # add data passed in to new node, point to head node next
        new_node = Node(data, self.head)
        # update head node to new node
        self.head = new_node


# linked list implementation
ll = LinkedList()
ll.insert_beginning("data")

ll.print_linkedlist()   # data1 -> None