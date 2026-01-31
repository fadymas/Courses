d_g={
    1:[2,3],
    2:[3],
    3:[],
    4:[3]
}
def adg_m(g,n):
    matrix = [[0 for _ in range (n)] for _ in range (n)]
    for u in g :
        for v in g[u]:
            matrix[u-1][v-1] = 1 
    return matrix

matrix = adg_m(d_g,4)
for row in matrix:
    print(row)