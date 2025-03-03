
class Stack:
    def __init__(self, max_length=None):
        self.stack = []
        self.max_length = max_length

    def push(self, value):
        if self.full():
            raise Exception
        self.stack = [value] + self.stack            

    def pop(self):
        if self.full():
            raise Exception
        del self.stack[0]

    def peek(self):
        if self.empty():
            raise Exception
        return self.stack[-1]

    def empty(self):
         return len(self.stack) == 0 

    def full(self):
        if self.empty():
            raise Exception("Stack is empty")
        return len(self.stack) >= self.max_length

    def __len__(self):
        return len(self.stack)

    def __contains__(self, item):
        if item in self.stack:
            return item

    def __eq__(self,stack2):
        return self.stack == stack2.stack

mystack = Stack()
