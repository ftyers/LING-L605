

# Helper function for recursive level order traversal
def levelOrderRec(root, level, res):
	if not root:
		return

	# Add a new level to the result if needed
	if len(res) <= level:
		res.append([])

	# Add current node's data to its corresponding level
	res[level].append(root.value)

	# Recur for left and right children
	levelOrderRec(root.left, level + 1, res)
	levelOrderRec(root.right, level + 1, res)

# Function to perform level order traversal
def levelOrder(root):
	res = []
	levelOrderRec(root, 0, res)
	return res

class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None 


	def insert(self, value):

		if self.value > value:			# key belongs in left subtree 
			if self.left:
				self.left.insert(value)
			else:					   # left subtree is empty
				self.left = Node(value)
		else:						   # key belongs in right subtree 
			if self.right:
				self.right.insert(value)
			else:					   # right subtree is empty
				self.right = Node(value)

	def find(self, needle):
		if needle == self.value:
			return self

		if needle < self.value:
			if self.left:
				return self.left.find(needle)
		else:
			if self.right:
				return self.right.find(needle)

       
	def delete(self, value):
		if self.value == value: # We found the value
			if not self.right:
				return self.left
			if not self.left:
				return self.right

			if self.right and self.left:
			# This is the hard case, the node has both children
			# We want the leftmost successor from the right subtree
				[parent, successor] = self.right._min(self) # We pass the current node as second argument
				print('P:',parent,'S:', successor, 'SR:',successor.right)
				
				if parent.left == successor:
					parent.left = successor.right
				else:
					parent.right = successor.right
				
				successor.left = self.left
				successor.right = self.right

				return successor
		else:
			if self.value > value: # It must be in the left subtree
				if self.left:
					self.left = self.left.delete(value)
			else:
				if self.right:
					self.right = self.right.delete(value)

		return self

	def _min(self, parent):
		if self.left:
			return self.left._min(self)
		else:
			return [parent, self]

	def __str__(self):
		return "[" + str(self.value) + "]"

class BinarySearchTree:
	def __init__(self):
		self.root = None
		
	def insert(self, value):
		if self.root:
			self.root.insert(value)
		else:
			self.root = Node(value)

	def inorder(self, level, node=None):
		if node:
			self.inorder(level+1, node.left)
			print(" " * level, node.value, end="\n")
			self.inorder(level+1, node.right)

	def postorder(self, node=None):
		if node:
			self.postorder(node.left)
			self.postorder(node.right)
			print(node.value, end=" ")


	def preorder(self, node=None):
		if node:
			print(node.value, end=" ")
			self.preorder(node.left)
			self.preorder(node.right)


	def delete(self, value):
		if self.root:
			self.root = self.root.delete(value)
 
	def find(self, needle):
		if self.root:
			return self.root.find(needle)


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


if __name__ == "__main__":
	b = BinarySearchTree()
	#b.insert(10)
	#b.insert(100)
	#b.insert(50)
	#b.insert(25)
	#b.insert(5)
	#b.insert(200)
	#b.insert(400)
	#b.insert(150)
	#b.insert(1)
	#for i in [35, 80, 20, 81, 16, 67, 21, 53, 67, 49, 27, 97, 76, 66, 68]:
	for i in [35, 80, 20, 81, 16, 67, 21, 53, 72, 49, 27, 97, 76, 66, 70]:
		b.insert(i)
		b.pretty()
#	b.insert(16)
#	b.insert(7)
#	b.insert(9)
#	b.insert(4)
#	b.insert(49)
#	b.insert(25)
#	b.insert(64)
#	b.insert(1)
#	b.insert(52)
#	b.insert(81)
#	
#	print('In:')
#	b.inorder(0, b.root)
#	print()
#	print('Pre:')
#	b.preorder(b.root)
#	print()
#	print('Post:')
#	b.postorder(b.root)
		print()
	#	PrintTree(b.root)
		b.pretty()
		print()
	
	
	b.delete(27)
	print()
	#PrintTree(b.root)
	b.pretty()
	print()
	
	
	b.delete(81)
	print()
	#PrintTree(b.root)
	b.pretty()
	print()
	
	
	b.delete(67)
	
	print()
	#PrintTree(b.root)
	b.pretty()
	print()
	
	b.delete(66)
	
	print()
	#PrintTree(b.root)
	b.pretty()
	print()
	
	
	b.delete(70)
	
	print()
	#PrintTree(b.root)
	b.pretty()
	print()
	


#	
#	print('DELETE 4:')
#	b.delete(4)
#	b.inorder(0, b.root)
#	print()
#	PrintTree(b.root)
#	print()
#	
#	print('DELETE 49:')
#	b.delete(49)
#	b.inorder(0, b.root)
#	print()
#	PrintTree(b.root)
#	print()
#	
#	print('DELETE 7:')
#	b.delete(7)
#	b.inorder(0, b.root)
#	print()
#	PrintTree(b.root)
#	print()
#	
#	print('DELETE 16:')
#	b.delete(16)
#	b.inorder(0, b.root)
#	print()
#	PrintTree(b.root)
#	print()
#	
	
	print(levelOrder(b.root))
