import heap as Heap

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def insert(self, node):
        self.nodes.add(node)        
        if node not in self.edges:
            self.edges[node] = set()

    def link(self, from_, to, weight=1):
        self.edges[from_].add((to, weight))

    def show(self):
        for n in self.nodes:
            print(n, self.edges[n])

    def bestfirst(self, source, target):
        pq = Heap()
        e = QueueElement(source, 0)        
        visited=set()

        pq.insert(e)

        while not pq.empty():
            current = pq.delete().value
            visited.insert(current)
            if current in visited:
                continue
            elif current == target: 
                return current
            

class QueueElement:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __eq__(self, other):      
        return self.priority == other.priority

if __name__ == '__main__':
    g = Graph()
    for node in 'ABCDEFGHI':
        g.insert(node)

    edges = [
    ('A', 'B', 1),
    ('A', 'D', 3),
    ('B', 'C', 5),
    ('B', 'E', 1),
    ('C', 'I', 1),
    ('D', 'C', 1),
    ('D', 'I', 3),
    ('E', 'F', 2),
    ('F', 'G', 3),
    ('F', 'H', 2),
    ('F', 'I', 1),
    ('G', 'H', 4)]


    for from_, to, weight in edges:
        g.link(from_, to, weight)

    g.show()
