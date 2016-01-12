class Node(Object):

    def __init__(self, data=Null, next=Null):
        self.data = data
        self.next = next

    def getData(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self,new_next):
        self.next = new_next


class LinkedList(Object):

    def __init__(self,head=Null):
        self.head = head

    def insert(self,data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    

list = new LinkedList(Null)

list.insert(3)
