# implement this for hw

class Queue:
    def __init__(self, max_length):
        self.queue = []
        self.max_length = max_length

    def enqueue(self, val):
        if self.full():
            raise Exception
        else:
            self.queue = self.queue + [val]

    def dequeue(self):
        if self.empty():
            raise Empty
        del self.queue[-1]
                  
    def head(self):
        if self.empty():
            raise Exception("Queue is empty")
        return self.queue[0]

    def tail(self):
        if self.empty():
            raise Exception("Queue is empty")
        return self.queue[-1]

    def empty(self):
        return len(self.queue) == 0

    def full(self):
        return len(self.queue) == self.max_length

    def __str__(self):
        return '| %d QUEUE %d %s' % (self.max_length, len(self.queue), self.queue)

