class Stack:
    def __init__(self, max_length):   # constructor
        self.stack = []
        self.max_length = max_length

    def push(self, value):   # methods
        if self.full() == True:
          return "Stack is full!"
        else:
          self.stack =  self.stack + [value]

    def pop(self):
        if self.empty() == True:
           return "Stack is empthy!"
        else:
          self.stack = self.stack[:-1]

    def peek(self):
        length = len(self.stack)-1
        return print(self.stack[length])

    def empty(self):
        if len(self.stack) == 0:
          return True
        return False

    def full(self):
        if len(self.stack) == self.max_length:
          return True
        return False

    def __eq__(self1, self2):
        equal_val = True
        for i in range(len(self1.stack)):
            if self1.stack[i] != self2.stack[i]:
                equal_val = False
        return equal_val

        # return self.stack == other.stack

    def __len__(self):
        for i in self.stack:
            if self1.stack[i] != self2.stack[i]:
                equal_val = False
        return equal_val


        # return len(self.stack)

    def __contains__(self, value):
        return value in self.stack

    def __str__(self):
        return str(self.stack)

    #
