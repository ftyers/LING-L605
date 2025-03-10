import math 

class Heap:
    def __init__(self):
        self.nodes = []

    def insert(self, value):
        print(f'Inserting {value}')
        self.nodes.append(value)
        self._up(len(self.nodes)-1)

    def delete(self,value):
        print(f'Deleting {value}')
        if self.empty():
            raise Exception("Heap is empty!")
        if value not in self.nodes:
            raise Exception(f"{value} is not in Heap!")
        
        index = self.nodes.index(value)  # Get the index of the value
        last_element = self.nodes.pop()  # Remove last element

        if index < len(self.nodes): 
            self.nodes[index] = last_element
            parent_i = (index - 1) // 2
            if index > 0 and self.nodes[index] < self.nodes[parent_i]:
                self._up(index)  # send up if value smaller than parent
            else:
                self._down(index)  # send down if value larger than children
        
        print(f"Deleted {value}, Updated Heap: {self.nodes}")


    def _up(self, index):
        while index > 0:
            parent_i = (index - 1) // 2
            if self.nodes[parent_i] > self.nodes[index]:  # Min-heap
                self.nodes[parent_i], self.nodes[index] = self.nodes[index], self.nodes[parent_i]
                index = parent_i
            else:
                break

    def peek(self):
        return self.nodes[0] if not self.empty() else None
    
    def poll(self):
        if self.empty():
            raise Exception("Heap is empty!")
        top_element = self.nodes[0]
        last_element = self.nodes.pop()  # Remove last element
        if self.nodes:
            self.nodes[0] = last_element  # Replace root
            self._down(0)
        return top_element
    
    def _down(self, index):
        left = (index * 2) + 1
        right = (index * 2) + 2
        smallest = index
        size = len(self.nodes)
        
        if left < size and self.nodes[left] < self.nodes[smallest]:
            smallest = left
        if right < size and self.nodes[right] < self.nodes[smallest]:
            smallest = right
        if smallest != index:
            self.nodes[index], self.nodes[smallest] = self.nodes[smallest], self.nodes[index]
            self._down(smallest)
    
    def print_tree(self):
        if not self.nodes:
            raise Exception("Heap is empty!")

        
        levels = math.floor(math.log2(len(self.nodes))) + 1  # Number of levels
        max_width = 2 ** levels  

        index = 0
        for level in range(levels):
            num_nodes = 2 ** level  # Number of nodes at this level
            spacing = " " * (max_width // (num_nodes + 1)) 
            
            row_values = []
            for _ in range(num_nodes):
                if index < len(self.nodes):
                    row_values.append(str(self.nodes[index]))
                    index += 1
                else:
                    break

            print(spacing + spacing.join(row_values))  # Print nodes with spacing

    def empty(self):
        return len(self.nodes) == 0


heap_example = Heap()
for value in [4, 17, 8, 13, 54, 33, 10, 7, 99, 25]:
    heap_example.insert(value)
    # print(heap_example)

heap_example.print_tree()

a = heap_example.poll()

print(a)
print(heap_example.nodes)

heap_example.print_tree()

