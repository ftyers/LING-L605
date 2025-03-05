import stack
import queue

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

        def __str__(self):
            out = "graph G {\n"
            for i in self.edges:
                for j in self.edges[i]:
                    out += "%d -- %d\n" % (i, j)
            out += "}\n"
            return out
        
        def dfs(self, current=0, visited=set()):
            #make a next stack
            s = stack.Stack(20)
            #push the current node
            s.push(current)
            #while the stack is not empty
            while not s.empty():
                #pop the top of the stack
                current = s.pop()
                #if it has been visited, continue
                if current in visited:
                    continue
                #otherwise add it to visited
                visited.add(current)
                #print the node
                print("Visited:", current)
                #for each child/neighbor
                for neighbor in self.edges[current]:
                    #if the neighbor is not visited
                    if neighbor not in visited:
                    #push the neighbor to the stack
                        s.push(neighbor)

        def bfs(self, current=0, visited=set()):
            q= queue.Queue(20)
            #enqueue current node
            q.enqueue(current)
            visited.add(current)
            #while the queue is not empty
            while not q.empty():
                #dequeue the head of the queue
                current = q.dequeue()
                #print
                print("Visited:", current)
                #for each child
                for child in self.edges[current]:
                    #if not visited
                    if child not in visited:
                        #enqueue child
                        q.enqueue(child)
                        #add to visited
                        visited.add(child)

g = Graph()
for i in range(0,6):
    g.insert(i)

#print(g.nodes)
#print(g.edges)

edges = [(0,1), (0,2), (1,3), (1,4), (2,4), (2,5), (4,5)]
my_edges = [(2, 3), (4, 2), (2, 5), (1, 3), (5, 1), (3, 0), (2, 1), (0, 4)]

for i,j in my_edges:
    g.link(i,j)

#print(g.nodes)
#print(g.edges)
# https://dreampuf.github.io/GraphvizOnline/?
# dot -Tpng -ograph.png < graph.txt
print(g)
g.bfs()
