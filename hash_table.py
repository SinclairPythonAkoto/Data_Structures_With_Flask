class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size    # creates a list of None values 

    # convert dict-key to ASCII int
    def custom_hash(self, key):
        hash_value = 0
        for char in key:
            # convert character to ASCCI int
            hash_value = ord(char)
            # turn hash value into unique number 
            hash_value = (hash_value * ord(char)) % self.table_size
        return hash_value
    
    def add_key_value(self, key, value):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is None:
            # add node to empty hash key
            self.hash_table[hashed_key] = Node(Data(key, value), None)
        else:
            # if a node already exists in hash key
            node = self.hash_table[hashed_key]
            while node.next_node:
                node = node.next_node
            # add new data at end of linked list
            node.next_node = Node(Data(key, value), None)

    def get_value(self, key):
        hashed_key = self.custom_hash(key)
        # check if hashed key is in hashmap
        if self.hash_table[hashed_key] is not None:
            # create node instance using hashed key
            node = self.hash_table[hashed_key]
            # check if the next node is empty
            if node.next_node is None:
                return node.data.value
            # check if next node's key is a match
            # this only runs if next node is not empty
            while node.next_node:
                # else move onto next node
                if key == node.data.key:
                    return node.data.value
                node = node.next_node

            # check if node if has equal key
            if key == node.data.key:
                return node.data.value
        return None
    
    def print_table(self):
        print("{")
        for index, val in enumerate(self.hash_table):
            if val is not None:
                llist_string = ""
                node = val
                if node.next_node:
                    while node.next_node:
                        llist_string += (
                            str(node.data.key) + " : " + str(node.data.value) + " --> "
                        )
                        node = node.next_node
                    llist_string += (
                        str(node.data.key) + " : " + str(node.data.value) + " --> None"
                    )
                    print(f"    [{index}] {llist_string}")
                else:
                    print(f"    [{index}] {val.data.key} : {val.data.value}")
            else:
                print(f"    [{index}] {val}")
        print("}")


# implementation
# ht = HashTable(4)
# ht.add_key_value("hi", "there")
# ht.add_key_value("hi", "there")
# ht.add_key_value("hi", "there")
# ht.add_key_value("python", "akoto")
# ht.print_table()

# {
#     [0] python : akoto
#     [1] hi : there --> hi : there --> hi : there --> None
#     [2] None
#     [3] None
# }