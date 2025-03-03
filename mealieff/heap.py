# min-heap: smallest value always at the root

import math

class Heap:
    def __init__(self):
        self.nodes = []

    def index(self, i):
        for i in range(len(self.nodes)):
             index +=i

    def insert(self, value):
        self.nodes.append(value)
        self._up()
        pass

    def _up(self, child=None):
        if child is None:
            child = len(self.nodes) - 1
        if child == 0:
            return

        parent = (child - 1) // 2
        if self.nodes[child] < self.nodes [parent]:   
            self.nodes[parent], self.nodes[child] = self.nodes[child], self.nodes[parent]
            self._up(parent)

    def delete(self):
        if len(self.nodes) == 0:
            return

        # Delete root node
        self.nodes[0], self.nodes[-1] = self.nodes[-1], self.nodes[0] 
        min_value = self.nodes.pop()
        self._down(0)
        return min_value


    def _down(self, parent):
        left = 2 * parent + 1
        right = 2 * parent + 2

        min_value = parent

        if left < len(self.nodes) and self.nodes[left] < self.nodes[min_value]:
            min_value = left
        if right < len(self.nodes) and self.nodes[right] < self.nodes[min_value]:
            min_value = right

        if min_value != parent:
             self.nodes[parent], self.nodes[min_value] = self.nodes[min_value], self.nodes[parent]
             self._down(min_value)

    def peek(self):
        if self.empty(): return None
        return self.nodes[0]

    def empty(self):
        # If the heap is empty, return True, otherwise False
        if len(self.nodes) == 0:
            return True
    
    def printHeap(self, total_width=60, fill=' '):
        """Pretty-print the heap tree structure."""
        if not self.nodes:
            print("(empty heap)")
            return
        
        output = []
        last_row = -1
        for i, n in enumerate(self.nodes):
            row = int(math.log2(i + 1))  # Compute tree depth
            
            if row != last_row:
                output.append("\n")  # New line at each tree level
            
            columns = 2**row  # Number of elements at this level
            col_width = max(1, total_width // columns)  # Adjust width dynamically
            
            output.append(str(n).center(col_width, fill))
            last_row = row
        
        print("-" * total_width)
        print("".join(output))
        print("-" * total_width)


heap = Heap()
s = [11, 24, 66, 44, 6, 19, 8, 12]

for num in s:
    heap.insert(num)
    heap.printHeap()

while not heap.empty():
    heap.delete()
    heap.printHeap()
