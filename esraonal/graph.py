from stack import Stack
from queue import Queue
from heap import Heap

class QueueElement:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
    def __lt__(self, other):
        return self.weight < other.weight
    def __eq__(self, other):
        return self.weight == other.weight
    def __gt__(self, other):
        return self.weight > other.weight
    def __str__(self):
        return f"QueueElement(value={self.value}, weight={self.weight})"
    
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def insert(self, value):
        self.nodes.add(value)
        if value not in self.edges:
            self.edges[value] = set()

    def link(self, n1, n2, weight=1):
        if n1 in self.nodes and n2 in self.nodes:
            self.edges[n1].add((n2, weight))
            # self.edges[n2].add((n1, weight))
        return
    
    def show(self):
        for n in self.nodes:
            print(n, self.edges[n])
    
    def bestfirst(self, source, target):
        priority_queue = Heap()
        visited = set()

        e = QueueElement(source, 0)
        # print(str(e))
        priority_queue.insert(e)

        while not priority_queue.empty():
            current = priority_queue.poll().value
            print(current, '///', priority_queue)
            # print(current)
            visited.add(current)
            if current == target:
                return current
            for n, w in self.edges[current]:
                # print(str(n) + str(w))
                if n not in visited:
                    e = QueueElement(n, w)
                    priority_queue.insert(e)

        return None 
    
    def dfs(self, current=0, visited=set()):
        # make a new stack
        stack = Stack(6)
        # push the current node
        stack.push(current)

        # while the stack is not empty
        while not stack.empty():
            # pop the top of the stack -> current
            current = stack.pop()
            # if it has been visited, continue
            if current in visited:
                continue
            # otherwise add it to visited
            visited.add(current)
            # DO SOMETHING <e.g. print the node>
            print('VISITED:', current)
            # for each child/neighbour  // self.edges[current]
            for c, w in self.edges[current]:
                # if the neighbour is not visited
                if c not in visited:
                    # push the neighbour to the stack
                    stack.push(c)
        return
    
    def beam_search(self, source, target, beta=2):
        beam = [(source, [source], 0)]
        while beam:
            # print("Beam ", beam)
            next_beam = []
            for node, path, score in beam:
                if node == target:
                    return node, path, score
                
                for neighboor, weight in self.edges[node]:
                    current = (neighboor, path + [neighboor], score + weight)
                    # print("Current: ", current)
                    next_beam.append(current)

            print("Next beam", next_beam)
            beam = sorted(next_beam, key=lambda x: x[2])
            beam = beam[:beta]

    
    def bfs(self, current=0, visited=set()):
        q = Queue(6)
        q.enqueue(current)
        visited.add(current)
        while not q.empty():
            current = q.dequeue()
            print('VISITED:', current)
            for c, w in self.edges[current]:
                # if the neighbour is not visited
                if c not in visited:
                    # push the neighbour to the stack
                    q.enqueue(c)
                    visited.add(c)

        return

    def __str__(self):
        out = "graph G {\n"
        for i in self.edges:
            for j in self.edges[i]:
                out += "%d -- %d\n" % (i, j)
        out += "}\n"
        return out
    

# g = Graph()
# for i in range(0,6):
#     g.insert(i)

# print(g.nodes)
# print(g.edges)

# for i, j in [(2, 3), (4, 2), (2, 5), (1, 3), (5, 1), (0, 3), (2, 1), (0, 4)]:
#     g.link(i, j)

# print(g.nodes)
# print(g.edges)

# g.dfs()
# g.bfs()

# g = Graph()
# for node in 'ABCDEFGHI':
#     g.insert(node)

# edges = [
# ('A', 'B', 1),
# ('A', 'D', 3),
# ('B', 'C', 5),
# ('B', 'E', 1),
# ('C', 'I', 1),
# ('D', 'C', 1),
# ('D', 'I', 3),
# ('E', 'F', 2),
# ('F', 'G', 3),
# ('F', 'H', 2),
# ('F', 'I', 1),
# ('G', 'H', 4)]


# for from_, to, weight in edges:
#     g.link(from_, to, weight)

# g.show()

# # g.dfs()
# res = g.beam_search('A', 'G')
# print(res)
