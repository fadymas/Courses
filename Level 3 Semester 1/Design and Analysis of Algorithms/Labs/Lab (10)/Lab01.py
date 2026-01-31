def createGraph(V, edges):
    mat = [[0 for _ in range(V)] for _ in range(V)]

    
    for it in edges:
        u = it[0]
        v = it[1]
        mat[u][v] = 1
 
    return mat

if __name__ == "__main__":
    V = 3

    
    edges = [[1, 0], [2, 0], [1, 2]]

    
    mat = createGraph(V, edges)

    print("Adjacency Matrix Representation:")
    for i in range(V):
        for j in range(V):
            print(mat[i][j], end=" ")
        print()