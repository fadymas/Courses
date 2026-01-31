d_g={1:[2,3],
     2:[3],
     3:[],
     4:[3]
     }
def bfs(g,start):
    visited= set()
    queue= [start]
    print ("BFS", end=" ")
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for nei in g[node]:
                queue.append(nei)
    print()
bfs(d_g,1)
bfs(d_g,4)