# undirected 

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

    def link(self, from_, to):
        self.edges[from_].add(to)

    def dfs(self, current=0, visited=set(), visiting=set(),  depth=0):
        depth =+ 1
        print(' '* depth, current)
        if self.node in visiting:
            return
        
        for neighbor in self.edges[current]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)
            
        visited.add(current)

    def dfs_stack(self, current=0, visited=set()):
        # Make a new stack
        s = Stack(maxlen=10)
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
            print("DFS time")
            print('VISITED:', current)
            # for each child/neighbour  // self.edges[current]
            for c in (list(self.edges[current])):
                # if the neighbour is not visited
                if c not in visited:
                    # push the neighbour to the stack
                    s.push(c)

    def bfs(self, current=0, visited=set()):
        q = Queue(max_length=10)
        q.enqueue(current)
        while not q.empty():
            current = q.dequeue()
            if current in visited:
                continue
            visited.add(current)
            print("BFS time")
            print('VISITED:', current, self.edges[current])
            for c in self.edges[current]:
            # if the neighbour is not visited
                if c not in visited:
                    q.enqueue(c)

    def __str__(self):
        out = "graph G {\n"
        for i in self.edges:
            for j in self.edges[i]:
                out += "%d -- %d\n" % (i, j)
        out += "}\n"
        return out

g = Graph()
#for i in range(0,6):
#    g.insert(i)

print(g.nodes)
print(g.edges)

graph = {
0:[3],
1:[],
2:[1,4],
3:[2,4,7],
4:[3],
5:[0],
6:[],
7:[5,6]
}

for n in graph:
    g.insert(n)
    for j in graph[n]:
        g.link(n,j)

print(g.nodes)
print(g.edges)

print('dfs time')
g.dfs()
#g.bfs(current=0)
