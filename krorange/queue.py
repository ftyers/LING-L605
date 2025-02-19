class Queue:
    def __init__(self, max_length):
        self.queue = []
        self.max_length = max_length

    def enqueue(self, value):
        if self.full():
            raise Exception
        self.queue = [value] + self.queue

    def dequeue(self):
        if self.empty():
            raise Exception
        value = self.queue[-1]
        del self.queue[-1]
        return value

    def head(self):
        if self.empty():
            raise Exception
        return self.queue[-1]

    def tail(self):
        if self.empty():
            raise Exception
        return self.queue[0]

    def full(self):
        if self.length() == self.max_length:
            return True
        return False

    def empty(self):
        if self.length() == 0:
            return True
        return False

    def length(self):
        return len(self.queue)

    def __str__(self):
        return '| %d QUEUE %d %s' % (self.max_length, len(self.queue), self.queue)