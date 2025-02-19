class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def insert(self, value):
		if value < self.value:
			if self.left:
				self.left.insert(value)
			else:
				self.left = Node(value)
		else:
			if self.right:
				self.right.insert(value)
			else:
				self.right = Node(value)

	def inorder(self, height):
		if self.left:
			self.left.inorder(height + 1)
		print(height, self.value)
		if self.right:
			self.right.inorder(height + 1)

	def find(self, value):
	# traverse the graph
	# return the value if found, otherwise None
		if value == self.value:
			if value < self.value:
				print(f'There is', value)
				return self.left.find(value)
			else:
				print(f'There is', value)
				return self.right.find(value)
		else:
			return None

	def delete(self, value):
		if value < self.value:
			if self.left:
				self.left = self.left.delete(value)
				rightmost = self.left.find(value.right.child)
				self.left = rightmost
				return self.left
		else:
			if self.right:
				self.right = self.right.delete(value)
				leftmost = self.right.find(value.left.child)
				self.right = leftmost
				return self.right
		return self

	def __str__(self):
		return '['+str(self.value)+']'

class BinarySearchTree:
	def __init__(self):
		self.root = None

	def insert(self, value):
		if self.root: # If we have already defined the root
			# call the insert function of the root node
			self.root.insert(value)
		else:    # define the root
			self.root = Node(value)

	def inorder(self):
		height = 0
		if self.root:
			self.root.inorder(height)

	def find(self, value):
		if self.root:
			self.root.find(value)

	def delete(self, value):
		if self.root:
			self.root.delete(value)
	
	def pretty(self):
		root = self.root
		def height(root):
			return 1 + max(height(root.left), height(root.right)) if root else -1  
		nlevels = height(root)
		width =  pow(2,nlevels+1)
    
		q=[(root,0,width,'c')]
		levels=[]
    
		while q:
			node, level, x, align = q.pop(0)
			if node:            
				if len(levels) <= level:
					levels.append([])
            
				levels[level].append([node,level,x,align])
				seg= width // (pow(2, level+1))
				q.append((node.left, level+1, x - seg, 'l'))
				q.append((node.right, level+1, x + seg, 'r'))
    
		for i, l in enumerate(levels):
			pre = 0
			preline = 0
			linestr = ''
			pstr = ''
			seg = width // (pow(2, i+1))
			for n in l:
				valstr = str(n[0].value)
				if n[3] == 'r':
					linestr += ' ' * (n[2] - preline - 1 - seg - seg // 2) + '¯' * (seg + seg // 2) + '\\'
					preline = n[2] 
				if n[3] == 'l':
					linestr += ' ' * (n[2] - preline - 1) + '/' + '¯' * (seg + seg // 2)  
					preline = n[2] + seg + seg // 2
				pstr += ' ' * (n[2] - pre - len(valstr)) + valstr #correct the potition acording to the number size
				pre = n[2]
			print(linestr)
			print(pstr)

b = BinarySearchTree()
for i in [35, 80, 20, 81, 16, 67, 21, 53, 72, 49, 27, 97, 76, 66, 70]:
	b.insert(i)

b.pretty()

b.inorder()

b.find(35)
b.find(1)

b.delete(27)
b.delete(81)
b.delete(67)