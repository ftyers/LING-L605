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
		# make a new node
		new_node = Node(value)
		# if head is None: make new node head
		if self.head == None:
			self.head = new_node
			return

		# iterate to the end of the list (while, None) current_node
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

	def find(self, value):
		current_node = self.head
		while current_node != None:
			if current_node.data == value:
				return True
			current_node = current_node.next
		return False

	def insert(self, index, value):
		if (index == 0):
			self.prepend(value)
			return
		
		pre = self.at(index - 1)
		post = pre.next
		node = Node(value)
		pre.next = node
		node.next = post

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

	def update(self, index, value):
		current = self.head
		i = 1
		while i < index and current is not None:
			current = current.next
			i += 1
		current.data = value
			
	def __len__(self):
		return self.length()

	def __getitem__(self, index):
		node = self.head
		if index > len(self):
			raise Exception
		for i in range(len(self)):
			if i == index:
				return node.data
			node = node.next

	def __str__(self):
		s = '' 
		# set the current node to be the head
		node = self.head
		# iterate until you find the end of the list
		while node.next:
			# the string is the concatenation of all 
			# element values
			s += node.data
			# move onto the next node
			node = node.next
		# append the final value
		s += node.data
		return s

