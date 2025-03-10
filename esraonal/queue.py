class Queue:
    def __init__(self, max_length):
        self.queue = []
        self.max_length = max_length

    def enqueue(self, value):
        if self.full():
            raise Exception("Queue is full!")
        self.queue = [value] + self.queue
        # [2, 3, 5]
        # [[6], 2, 3, 5]

    def dequeue(self):
        if self.empty():
            raise Exception("Queue is empty!")
        dequeued_item = self.queue[-1]
        self.queue = self.queue[:-1]
        # [6, 2, 3, [5]]
        # [6, 2, 3]
        return dequeued_item

    def head(self):
        if self.empty():
            raise Exception("Queue is empty!")
        return self.queue[-1]

    def tail(self):
        if self.empty():
            raise Exception("Queue is empty!")
        return self.queue[0]

    def full(self):
        return self.length() == self.max_length

    def empty(self):
        return self.length() == 0

    def length(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)
