def bfs(adj):
    V = len(adj)
    visited = []
    for i in range(V):
        visited.append(False)
    res = []
    queue = []
    front = 0
    src = 0
    visited[src] = True
    queue.append(src)
    while front < len(queue):
        curr = queue[front]
        front += 1
        res.append(curr)
        neighbors = adj[curr]
        for i in range(len(neighbors)):
            x = neighbors[i]
            if not visited[x]:
                visited[x] = True
                queue.append(x)
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
    res = bfs(adj)
    for node in res:
        print(node, end=" ")
