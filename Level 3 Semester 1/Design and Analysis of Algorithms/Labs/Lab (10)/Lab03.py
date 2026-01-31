def dfsRec(adj, visited, s, res):
    visited[s] = True
    res.append(s)
    for i in adj[s]:
        if not visited[i]:
            dfsRec(adj, visited, i, res)
            
def dfs(adj):
    visited = [False] * len(adj)
    res = []
    dfsRec(adj, visited, 0, res)
    return res

def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)
    
    
if __name__ == "__main__":
    V = 5
    adj = []
    
    for i in range(V):
        adj.append([])
        
    addEdge(adj, 1, 2)
    addEdge(adj, 1, 0)
    addEdge(adj, 2, 0)
    addEdge(adj, 2, 3)
    addEdge(adj, 2, 4)

    
    res = dfs(adj)

    for node in res:
        print(node, end=" ")