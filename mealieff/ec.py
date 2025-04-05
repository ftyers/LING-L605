###          Find Cycles and Output Them              ######
#                   Use Tiernan's method                          #
#      N should be determined programmatically      #

class Tiernan:
    def __init__(self, G, labels):
        self.labels = labels
        self.G = G

        # algorithm internal
        self.N = len(self.G)
        self.current_path = [] # path
        self.H = [[] for x in range(self.N)] # ?
        self.k = 0 # ?
        self.current_path.append(self.k)
    
    def tiernan(self): # find circuit
        self.path_extension()

    def path_extension(self): # path_extension
        #print('path_extension')
        canExpand = True
    
        while (canExpand == True):
            possible_expansions = []
            neighbours = self.G[self.current_path[self.k]]
            for neighbour in neighbours:
                if ((neighbour not in self.current_path) and 
                    (neighbour not in self.H[self.current_path[self.k]]) and 
                    (neighbour > self.current_path[0]) and 
                    (neighbour not in possible_expansions)):
                    possible_expansions.append(neighbour)
            #print("For vertex at index", k, "(", P[k],") in current path", P, "these are the possible expansions:", possible_expansions)
            print('k:', self.k, '/P[k]:', self.current_path[self.k], '/P:', self.current_path, '/pe:', possible_expansions, '/GPk:', neighbours, '/GPkj:',neighbour)
            if len(possible_expansions) == 0:
                canExpand = False
                if self.current_path[0] in self.G[self.current_path[self.k]]:
                    print("--> Hooray, cycle in", [self.labels[i] for i in self.current_path])
                self.vertex_closure()
            else:
                self.current_path.append(possible_expansions[0])
                self.k = self.k + 1
    
    def vertex_closure(self): # vertex closure

        if self.k == 0:
            self.advance_initial_vertex()
        else:
            self.H[self.current_path[self.k]] = []
            self.H[self.current_path[self.k - 1]].append(self.current_path[self.k])
            self.current_path.pop()
            self.k = self.k - 1;
            self.path_extension()
    
    def advance_initial_vertex(self): # advance initial vertex
        if self.current_path[0] == self.N - 1:
            print("Terminate")
        else:
            self.current_path[0] = self.current_path[0] + 1
            self.k = 0
            self.H = [[] for x in range(self.N)]
            self.path_extension()
    

# algorithm external
G = [[1],[1,2,3],[4],[2],[0]] # graph
labels = ['1', '2', '3', '4', '5']


t = Tiernan(G, labels)
t.tiernan()

