class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        newnode = Node(value)
        newnode.next = self.head
        self.head = newnode

    def append(self, value):
        newnode = Node(value)
        if self.head == None:
            self.head = newnode
            return

        current = self.head
        while current.next != None:
            current = current.next

        current.next = newnode

    def update_node(self, index, value):
        current = self.head
        i = 1
        while i < index and current is not None:
            current = current.next
            i += 1
        current.data = value
    
    def delete(self, index):
            # First check the bounds, if index > length of list, raise Exception
            if index > self.length():
                raise Exception

            # If the length is 0, raise Exception
            if self.length() == 0:
                raise Exception
    
            # Pre = node before the node to delete (index-1) 
            # Post = node after the node to delete (index+1) delete_node.next

            if index == 0:
                next_node = self.head.next
                del self.head
                self.head = next_node
                return

            # set the current_node to the head of the list
            current_node = self.head
            current_index = 0 # track the index we are at
            pre = None # the previous node
            while current_index < index - 1:
                current_node = current_node.next 
                current_index += 1
            pre = current_node
            target = current_node.next
            post = None
            if target:
                post = target.next
                del target
            pre.next = post
	
    def length(self):
        length = 0
        current_node = self.head
        while current_node != None:
            current_node = current_node.next
            length += 1
        return length

    def __str__(self):
        s = ''
        node = self.head
        while node.next != None:
            s += node.data
            node = node.next
        s += node.data
        return s


# mylist = LinkedList()
# mylist.pretend('p')
# mylist.pretend('a')
# mylist.pretend('h')
#
# print(mylist)
#
# mylist.append('r')
#
# print(mylist)
#
# mylist.append('y')
# mylist.append('u')
#
#
# print(mylist)
#
# mylist.update_node(3, 'k')
#
# print(mylist)

