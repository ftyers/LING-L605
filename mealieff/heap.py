class Heap:
    def __init__(self):
        self.nodes = []

    def parent(self, i):
        return (i-1)//2

    def left_child(self, i):
        return (2 * i) + 1

    def right_child(self, i):
        return (2 * i) + 2

    def index(self, i):
        for i in range(len(self.nodes)):
             index +=i

    def insert(self, value):
        self.nodes.append(value)
        self.heapify(len(self.nodes) - 1)

    def heapify(value, i):
        while True: 
            n_parent = self.parent(i)
            left = self.left_child(i)
            right = self.right_child(i)
            largest = i  #declaring this here assumes current node is the largest            
        
        # move a node up
        if i > 0 and self.nodes[i] > self.nodes[n_parent]:
            self.nodes[i], self.nodes[n_parent] = self.nodes[n_parent], self.nodes[i]
            i = n_parent
            continue  #iterate through as many times as needed 
## this continue part is an issue, i can't keep iterating through heapifying up before heapifying down if needed. might need to be two functions.

        # move a node down
        if left < len(self.nodes) and self.nodes[left] > self.nodes[largest]:
            largest = left
        if right < len(self.nodes) and self.nodes[right] > self.nodes[largest]:
            largest = right

        if largest == i:
            break
        self.nodes[i], self.nodes[largest] = self.nodes[largest], self.nodes[i]
        i = largest

    def peek(self):
        if self.empty(): return None
        return self.nodes[0]

    def empty(self):
        # If the heap is empty, return True, otherwise False
        if len(self.nodes) == 0:
            return True
    
    def printHeap(heap, total_width=60, fill=' '):
        import math
        """Pretty-print a tree.
        total_width depends on your input size"""
        output = ''
        last_row = -1
        for i, n in enumerate(heap):
            if i:
                row = int(math.floor(math.log(i+1, 2)))
            else:
                row = 0
            if row != last_row:
                output += '\n'
                #output.write('\n')
            columns = 2**row
            col_width = int(math.floor((total_width * 1.0) / columns))
            output+=str(n).center(col_width, fill)
            last_row = row
        print ('-' * total_width,end="")
        print (output)
        print ('-' * total_width)

heap = Heap()
s = [11, 24, 66, 44, 6, 19, 8, 12]

for num in s:
    heap.insert(num)
    heap.print_heap()
