class Stack: 
    def __init__(self, max_length):   # constructor
        self.stack = []
        self.max_length = max_length

    def push(self, value):
        if self.full(): # check if the stack is full
            raise Exception
        # append the value to the beginning of the list
        self.stack = [value] + self.stack
        #self.stack = self.stack + [value]
        #self.stack = self.stack.append(value)
        #self.stack = self.stack.insert(0, value)

    def pop(self):
        if self.empty(): 
            raise Exception
        value = self.stack[0]
        del self.stack[0]
        return value

    def peek(self):
        if self.empty():
            raise Exception
        return self.stack[0]

    def empty(self):
        if len(self.stack) == 0:    # return len(self.stack) == 0
            return True
        return False

    def full(self):
        if len(self.stack) == self.max_length:
            return True
        return False

    def __str__(self):
        return '| %d STACK %d %s' % (self.max_length, len(self.stack), self.stack)
    
    def __eq__(self, self2):
        if self.stack == self2.stack:
            return True
        return False
        
    def __contains__(self, value):
        if value in self.stack:
            return value

    def __len__(self):
        return len(self.stack)