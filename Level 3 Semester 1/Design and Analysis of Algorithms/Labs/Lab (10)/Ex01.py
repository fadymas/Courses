edges = [(1,2,5),
         (1,3,2),
         (2,3,4),
         (4,3,7)
         ]
def wei_adj_m(ed,n):
    matrix=[[0 for _ in range (n)] for _ in range (n) ]
    for u,v,w in ed:
        matrix[u-1][v-1]= w
    return matrix

matrix = wei_adj_m(edges,4)
for row in matrix:
    print(row)