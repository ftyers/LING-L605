
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
		output+= str(n).center(col_width, fill)
		last_row = row
	print ('-' * total_width,end="")
	print (output)
	print ('-' * total_width)

class MinHeap:
	def __init__(self):
		self.heap = []


	def peek(self):
		if self.empty():
			return 
		return self.heap[0]

	def empty(self):
		if len(self.heap) == 0:
			return True
		return False

	def poll(self):
		pass

	def heapify(self):
		printHeap(h.heap)
		print('##',len(self.heap), len(self.heap) // 2, len(self.heap) // 2 - 1)
		for i in range(len(self.heap) // 2 - 1, -1, -1):
			print('--> i:', i)
			self._heapify(i)
			printHeap(h.heap)
			print('--')

	def _heapify(self, i):
		print('--')
	
		n = len(self.heap)
		smallest = i # Assume smallest is current node
		left = 2 * i + 1 # Left child of current node
		right = 2 * i + 2 # Right child 

		print('1 _heapify: n', n, '| smallest:',  smallest, ' (',self.heap[smallest],')| i:', i, ' (',self.heap[i],')', end=" ")
		if left < n:
			print(' left:',  left, ' (', self.heap[left],')', end=" ")
		if right < n:
			print(' right:',  right, ' (', self.heap[right],')')
		print()

		# Is the left child smaller than the length of the heap and
		# is the value smaller than the current node
		if left < n and self.heap[left] < self.heap[smallest]:
			smallest = left

		# Check index bounds and then is the right child smaller?
		if right < n and self.heap[right] < self.heap[smallest]:
			smallest = right

		print('2 _heapify: n', n, '| smallest:',  smallest, ' (',self.heap[smallest],')| i:', i, ' (',self.heap[i],')', end=" ")
		if left < n:
			print(' left:',  left, ' (', self.heap[left],')', end=" ")
		if right < n:
			print(' right:',  right, ' (', self.heap[right],')')
		print()

		# If the smallest now is not the current, then we swap 
		# and check the subtree
		if smallest != i:
			# swap
			self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
			self._heapify(smallest)

		print('3 _heapify: n', n, '| smallest:',  smallest, ' (',self.heap[smallest],')| i:', i, ' (',self.heap[i],')', end=" ")
		if left < n:
			print(' left:',  left, ' (', self.heap[left],')', end=" ")
		if right < n:
			print(' right:',  right, ' (', self.heap[right],')')
		print()

	def _up(self, child=None):
		if not child:
			child = len(self.heap) - 1

#		print("%%%%%%%%%%%%")

#		printHeap(self.heap)

		parent = (child - 1) // 2
		if self.heap[parent] and self.heap[child] < self.heap[parent]:
			self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
			self._up(child=parent)


		return self.heap		

	def _down(self, index=0):
		n = len(self.heap)
		left = 2 * index + 1
		right = 2 * index + 2
		if index >= n or left > n:
			return self.heap

		smallest = None
		if left < n and self.heap[left] < self.heap[n - 1]:
			smallest = left
		if right < n and self.heap[right] < self.heap[left]:
			smallest = right

		if smallest == None:
			return self.heap
		
		print('1 _down |CUR:', index, '|', self.heap[index], '|SMAL:| idx:', smallest ,'| val:', self.heap[smallest], '|', self.heap)

		# If the current value is lower than both the children
		if self.heap[index] < self.heap[smallest]: # smallest_value:
			return self.heap

		print('2 _down |CUR:', index, '|', self.heap[index], '|SMAL:| idx:', smallest ,'| val:', self.heap[smallest], '|', self.heap)

		printHeap(self.heap)

		# Otherwise, swap the node with the smaller child and recurse
		if self.heap[index] > self.heap[smallest]:
			self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
			return self._down(smallest)

	def poll(self):
		if self.empty():
			return None

#		print('POLL()')
	
		# Copy the root (smallest) node
		root = self.heap[0]
		# Put the final node at the root
		self.heap[0] = self.heap[len(self.heap) - 1]
		# Delete the final nodes
		del self.heap[-1]
		# Run heapify down
		self._down()

		return root


	def insert(self, node):
#		print('insert', node)
		self.heap.append(node)
#		print('>', self.heap)
		self._up()
		print('<', self.heap)

	def __str__(self):
		return str(self.heap)


if __name__ == "__main__":
	
	h = MinHeap()
	
	#for i in [81, 64, 52, 49, 25, 16, 9, 7, 4, 1]:
	#	print('*'*80)
	#	h.insert(i)
	#	printHeap(h.heap)
	#
	#h.insert(100)
	
	
	
	#for i in [16, 7, 9, 4, 49, 25, 64, 1, 52, 81]:
	#for i in [4, 17, 8, 13, 54, 33, 10, 7, 99, 25]:
	#for i in [7, 99, 8, 4, 25, 10, 17, 54, 33, 13]:
	#pairs = [(4, 'C'), (7, 'D'), (13, 'G'), (10, 'F'), (8, 'E'), (54, 'X'), (17, 'I'), (99, 'K'), (25, 'M'), (33, 'Q')]
	
	for i in [4,7,13,10,8,54,17,99,25,33]:
		h.insert(i)
		printHeap(h.heap)
	
	print(h)
	
	#h.heapify()
	
	#print(h)
	
	#h.insert(5)
	
	#printHeap(h.heap)
	
	x = h.poll()
	
	printHeap(h.heap)
