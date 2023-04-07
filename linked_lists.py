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
        # check if head is empty
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head

        new_node = Node(data, self.head)
        self.head = new_node
    
    def insert_at_end(self, data):
        # if head is empty, instert into beginning
        if self.head is None:
            self.insert_beginning(data)

        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node



# linked list implementation
ll = LinkedList()
ll.insert_beginning("food1")
ll.insert_beginning("food2")
ll.insert_beginning("food3")
ll.insert_beginning("food4")
ll.insert_beginning("food5")
ll.insert_beginning("drinks1")
ll.insert_beginning("drinks2")

ll.insert_at_end("desert")
ll.insert_at_end("end")

ll.print_linkedlist()
# drinks2 -> drinks1 -> food5 -> food4 -> food3 -> food2 -> food1 -> desert -> end -> None