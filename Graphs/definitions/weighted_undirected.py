#directed, un-weighted graphs
class Graph:
    def __init__(self,num_nodes,edges):
        self.data = [[] for _ in range(num_nodes)]
        for v1,v2 in edges:
            self.data[v1].append(v2)
            self.data[v2].append(v1)
    
    def __repr__(self):
        return "\n".join(["{} : {}".format(i,neighbors) for i,neighbors in enumerate(self.data)])
    def __str__(self):
        return repr(self)
num_nodes6 = 5
edges6 = [(0, 1), (1, 2), (2, 3), (2, 4), (4, 2), (3, 0)]
g1  = Graph(num_nodes6,edges6)
print(g1)




