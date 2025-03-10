class Stack:
    def __init__(self, max_length):   
        self.stack = []
        self.max_length = max_length

    def push(self, value):   
        if self.full() == True:
          raise Exception("Stack is full!")
        self.stack =  self.stack + [value]

    def pop(self):
        if self.empty() == True:
           raise Exception("Stack is empty!")
        poped_item =  self.stack[-1] 
        self.stack = self.stack[:-1]
        return poped_item

    def peek(self):
        if self.empty():
            raise Exception("Stack is empty!")
        return self.stack[-1]

    def empty(self):
        return len(self.stack) == 0

    def full(self):
        return len(self.stack) == self.max_length

    def __eq__(self, other):
        return self.stack == other.stack

    def __len__(self):
        return len(self.stack)

    def __contains__(self, value):
        return value in self.stack

    def __str__(self):
        return str(self.stack)


