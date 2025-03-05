from stack import Stack
from queue import Queue

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def insert(self, value):
        self.nodes.append(value)
        if value not in self.edges:
            self.edges[value] = set()

    def link(self, from_, to):
        self.edges[from_].add(to)

    def dfs_(self, current=0, visited=set()):
        # Add the current node to the set of visited nodes
        visited.add(current)
        print(current) # do something
        # For each of its neighbours:
        neighbours = reversed(list(self.edges[current]))
        for neighbour in neighbours:
            # We check to see if we've already visited it
            if neighbour not in visited:
                # If not, we recursively visit it
                self.dfs(neighbour, visited)
                
    def dfs(self, current=0, visited=set()):
        # Make a new stack
        s = Stack(max_length=100)
        # push the current node
        s.push(current)
        # while the stack is not empty
        while not s.empty():
            # pop the top of the stack -> current
            current = s.pop()
            # if it has been visited, continue
            if current in visited:
                continue
            # otherwise add it to visited
            visited.add(current)
            # DO SOMETHING <e.g. print the node>
            print('VISITED:', current)
            # for each child/neighbour  // self.edges[current]
            #for c in list(self.edges[current]):
            for c in reversed(list(self.edges[current])):
                # if the neighbour is not visited
                if c not in visited:
                    # push the neighbour to the stack
                    s.push(c)

    def bfs(self, current=0, visited=set()):
        # Make a new queue
        q = Queue(max_length=100)
        # push the current node
        q.enqueue(current)
        # while the queue is not empty
        while not q.empty():
            # pop the top of the queue -> current
            current = q.dequeue()
            # if it has been visited, continue
            if current in visited:
                continue
            # otherwise add it to visited
            visited.add(current)
            # DO SOMETHING <e.g. print the node>
            print('VISITED:', current)
            # for each child/neighbour  // self.edges[current]
            #for c in reversed(list(self.edges[current])):
            for c in list(self.edges[current]):
                # if the neighbour is not visited
                if c not in visited:
                    # push the neighbour to the stack
                    q.enqueue(c)

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

#edges = [(0,1), (0, 2), (1,3), (2,1), (2,4), (3,4), (3,5), (4,5)] 
edges = [(0,1), (0,2), (1,3), (1,4), (2,4), (2,5), (4,5)]
for i, j in edges:
    g.link(i, j)

print(g.nodes)
print(g.edges)

print(g)

print('DFS:')
g.dfs(current=0)

print('\nBFS:')
g.bfs(current=0)