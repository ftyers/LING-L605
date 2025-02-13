class Stack:
	def __init__(self, maxlen):
		self.stack = []
		self.maxlen = maxlen

	def push(self, v):
		if self.full():
			raise Exception		
		self.stack = [v] + self.stack

	def pop(self):
		if self.empty():
			raise Exception
		val = self.stack[0]
		del self.stack[0]
		return val

	def peek(self):
		if self.empty():
			raise Exception
		return self.stack[0]

	def empty(self):
		if len(self.stack) == 0:
			return True
		return False
	
	def full(self):
		if len(self.stack) == self.maxlen:
			return True
		return False

	def __str__(self):
		return str(self.maxlen)+ ', '+ str(self.stack)

