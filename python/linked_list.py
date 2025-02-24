class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLinked_List:
    def __init__(self):
        self.head = None   
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data,end = "-->")
            curr = curr.next
        print("None")
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_at_end(self, data):
        curr = self.head
        new_node = Node(data)
        if curr is None:
            self.head = new_node
        while curr.next:
            curr = curr.next
            if curr.next is None:
                break
        curr.next = new_node
    def length(self):
        length = 0
        curr = self.head
        while curr:
            length += 1
            curr = curr.next
        return length
    def insert_node_at(self,data,pos):
        new_node = Node(data)
        curr = self.head
        count = 0
        while curr:
            if(count == pos):
                curr.next = new_node
                break
            count += 1
            curr = curr.next
if __name__ == "__main__":
    sll = SLinked_List()
    sll.insert_at_beginning(1)
    sll.insert_at_beginning(2)
    sll.insert_at_beginning(3)
    sll.insert_at_beginning(4)
    sll.insert_at_beginning(5)
    sll.print_list()
    sll.insert_node_at(10,3)
    sll.print_list()
        
            
            