class Heap:
	def __init__(self):
		self.nodes = []

	def insert(self, value):
		# Append the value to the list of nodes
		# Recursively swap the value upwards until we reach the right position
		n = len(self.nodes)
		self.nodes.append(value)
		self._up(n - 1)

	def _up(self, child=None):
		# If no child given, use the last item in the list
		n = len(self.nodes)
		if child == None:
			# last item
			child = n - 1
		while child > 0:
			# parent
			parent = (child - 1) // 2
			# Continue swapping while child is smaller than its parent
			if self.nodes[child] < self.nodes[parent]:
				# Swap child and parent
				self.nodes[child], self.nodes[parent] = self.nodes[parent], self.nodes[child]
				# Call up with the new parent index
				child = parent
			else:
				break

	def peek(self):
		if self.empty():
			return None
		return self.nodes[0]

	def empty(self):
		# If the heap is empty, return True, otherwise False
		if len(self.nodes) == 0:
			return True
		
	def printHeap(heap, total_width=60, fill=' '):
		import math
		"""Pretty-print a tree.
		total_width depends on your input size"""
		output = ''
		last_row = -1
		for i, n in enumerate(heap):
			if i:
				row = int(math.floor(math.log(i+1, 2)))
			else:
				row = 0
			if row != last_row:
				output += '\n'
				#output.write('\n')
			columns = 2**row
			col_width = int(math.floor((total_width * 1.0) / columns))
			output+=str(n).center(col_width, fill)
			last_row = row
		print ('-' * total_width,end="")
		print (output)
		print ('-' * total_width)

h = Heap()
h.insert(2)
h.printHeap()