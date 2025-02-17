class Queue:
    def __init__(self, max_length):
        self.queue = []
        self.max_length = max_length

    def enqueue(self, val):
        if self.full():
            raise Exception
        self.queue =  [val] + self.queue

    def dequeue(self):
        if self.empty():
            raise Exception
        val = self.queue[-1]
        del self.queue[-1]
        return val

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
        return str(self.queue)

    def __len__(self):
        l = 0
        for x in self.queue:
            l += 1
        return l

    def __eq__(self, self2):
        if len(self) != len(self2):
            return False
        for x in range(len(self)):
            if self.queue[x] != self2.queue[x]:
                return False
        return True

    def __contains__(self, self2):
        for e in range(len(self)):
            for ele in range(len(self2)):
                if self.queue[e] == self2.queue[ele]:


                    
