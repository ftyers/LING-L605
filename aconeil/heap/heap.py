import math

def printHeap(heap, total_width=60, fill=' '):
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


class Heap:
    def __init__(self):
        self.nodes = []
        

    def insert(self, value):
        #Append the value to the list of nodes
        #Recursively swap the value upwards until we reach the right position
        n = len(self.nodes)
        self.nodes.append(value)
        self._up(n-1)
        pass
   
    def poll(self):
        if self.empty():
            return None
        #get the root
        root = self.nodes[0]
        #put the last node at the root
        self.nodes[0] = self.nodes[-1]
        #delete the last node
        del self.nodes[-1]
        #run down
        self._down(index=0)

    def _down(self, index = 0):
        #find the child indexes
        left_in = 2*index +1
        right_in = 2*index +2
        left_child, right_child  = self.nodes[left_in], self.nodes[right_in]
        if left_child < right_child:
            if left_child > self.nodes[index]:
                self.nodes[left_in], self.nodes[index] = self.nodes[index], self.nodes[left_in]
                self._down(index+1)
        else:
            if right_child > self.nodes[index]:
                self.nodes[right_in], self.nodes[index] = self.nodes[index], self.nodes[right_in]
                self._down(index+1)
        #find the smallest of the children
        #if the smallest is greater, then swap and recurse


    def _up(self, child=None):
        #if no child given, use the last item in the list
        if not child:
            child = len(self.nodes) -1
        parent = (child -1) // 2
        #if the child is smaller than its parent
        if self.nodes[child] < self.nodes[parent]:
            #swap them
            self.nodes[child], self.nodes[parent] = self.nodes[parent],self.nodes[child]
        #call up the new parent
            self._up(child=parent)

    def peek(self):
        if self.empty():
            return None
        return self.nodes[0]

    def empty(self):
        #If the heap is empty, return True
        if len(self.nodes)==0:
            return True

h = Heap()

for i in [99, 54, 33, 25, 17, 13, 10, 8, 7, 4]:
    h.insert(i)

printHeap(h.nodes)
h.poll()
printHeap(h.nodes)
