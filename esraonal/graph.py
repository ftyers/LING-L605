from stack import Stack
from queue import Queue

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def insert(self, value):
        self.nodes.append(value)
        idx = len(self.nodes) - 1
        if idx not in self.edges:
            self.edges[value] = set()

    def link(self, n1, n2):
        if n1 in self.nodes and n2 in self.nodes:
            self.edges[n1].add(n2)
            self.edges[n2].add(n1)
    
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
            for c in self.edges[current]:
                # if the neighbour is not visited
                if c not in visited:
                    # push the neighbour to the stack
                    stack.push(c)
        return
    
    def bfs(self, current=0, visited=set()):
        q = Queue(6)
        q.enqueue(current)
        visited.add(current)
        while not q.empty():
            current = q.dequeue()
            print('VISITED:', current)
            for c in self.edges[current]:
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
    

g = Graph()
for i in range(0,6):
    g.insert(i)

print(g.nodes)
print(g.edges)

for i, j in [(2, 3), (4, 2), (2, 5), (1, 3), (5, 1), (0, 3), (2, 1), (0, 4)]:
    g.link(i, j)

print(g.nodes)
print(g.edges)

g.dfs()
# g.bfs()
