class Stack:
    def __init__(self, max_length):
        self.stack = []
        self.max_length = max_length

    def push(self, value):
        if self.full():
            raise Exception
        self.stack = [value] + self.stack

    def peek(self):
        if self.empty():
            raise Exception
        value = self.stack[0]
        return value

    def pop(self):
        if self.empty():
            raise Exception
        value = self.stack[0]
        del self.stack[0]
        return value

    def empty(self):
        if len(self.stack)==0:
            return True
        return False

    def full(self):
        if length(self.stack) == self.max_length:
            return True
        return False

    def length(self):
        l = 0
        for element in self.queue:
            l += 1
        return l
