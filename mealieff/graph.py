# undirected 

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

    def dfs(self, value, visited=False):
        if not visited:
           visited = set()

        if value not in visited:
            print(value, end=" ")               
            visited.add(value)
            print(value, visited)
        for neighbor in self.edges.get(value, []):
            self.dfs(neighbor, visited)

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

g.dfs(1)
g.dfs(4)
g.dfs(5)
