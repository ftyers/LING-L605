#boxes
class Node:
    
    def __init__(self, value):
        self.data = value
        self.next = None

#sequence of boxes
class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def prepend(self, value):
        # make a new node
        new_node = Node(value)
        #set the next element to be the head
        new_node.next = self.head
        #set self.head to be the new node
        self.head = new_node
   
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node

    def length(self):
        length = 0 
        current_node = self.head
        while current_node != None:
            current_node = current_node.next
            length += 1
        return length

    def __getitem__(self, index):
        node = self.head
        if index > len(self):
            raise Exception
        for i in range(len(self)):
            if i == index:
                return node.data
            node = node.next



    def __len__(self):
        return self.length()

    def __str__(self):
        s = ''
        node = self.head
        while node.next != None:
            s += node.data
            node = node.next
        s += node.data
    return s

mylist = LinkedList()
mylist.prepend('p')
mylist.prepend('a')
mylist.prepend('h')
mylist.prepend('c')
mylist.append('t')
mylist.append('e')
mylist.append('r')
print(mylist[3])

print(mylist)
