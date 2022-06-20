from Graphs.definitions.weighted_undirected import *
def dfs(graph,source):
    visited = [False] * len(graph.data)
    stack = [source]
    result = []
    traves = []

    while len(stack)>0:
        current = stack.pop()
        traves.append(current)
        if not visited[current]:
            result.append(current)
            visited[current] = True
            for v in graph.data[current]:
                stack.append(v)
    print(traves)
    return result

print(g1)

print(dfs(g1,1))    