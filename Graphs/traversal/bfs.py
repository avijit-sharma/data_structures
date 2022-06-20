from definitions.weighted_undirected import *
# in bfs we use queue to keep track of all the nodes visited and keep adding the all the
#neighbouring nodes to the queue inorder to trverse the whole graph

def bfs(graph,source):
    visited = [False] * len(graph.data)
    queue  = []
    visited[source] = True
    queue.append(source)
    i = 0
    while i < len(queue):
        for v in graph.data[queue[i]]:
            if not visited[v]:
                visited[v] = True
                queue.append(v) 
        i+=1
    return queue

print(bfs(g1,0))   


