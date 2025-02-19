# boxes
class Node:
	def __init__(self, value):
		self.data = value
		self.next = None

# sequence of boxes		
class LinkedList:
	def __init__(self):
		self.head = None

	def prepend(self, value):
		# make a new node
		new_node = Node(value)
		# set the next element to be the head
		new_node.next = self.head
		# and set head to be the new node
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
	
	def __len__(self):
		return self.length()
	
	def find(self, value):
		current_node = self.head
		index = 0
		while current_node is not None:
			if current_node.data == value:
				return index
			current_node = current_node.next
			index += 1
		return False

	def __str__(self):
		s = '' 
        # set the current node to be the head
		node = self.head
        # iterate until you find the end of the list
		while node.next != None:
            # the string is the concatenation of all 
            # element values
			s += node.data
            # move onto the next node
			node = node.next
        # append the final value
		s += node.data
		return s

mylist = LinkedList()
print(len(mylist))
mylist.prepend('p')
print(len(mylist))
mylist.prepend('a')
mylist.prepend('h')
mylist.prepend('c')
print(mylist)
print(len(mylist))

p = mylist.find('p')
print(f'Location of p: {p}')
f = mylist.find('f')
print(f'Location of f: {f}')

mylist.append('t')
mylist.append('e')
mylist.append('r')


print(mylist)
print(len(mylist))