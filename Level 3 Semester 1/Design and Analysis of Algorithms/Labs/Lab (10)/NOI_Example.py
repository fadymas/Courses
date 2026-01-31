def dfs(grid, i, j, rows, cols):
    stack = []
    stack.append([i, j])
    
    while stack:
        r, c = stack.pop()
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            continue
        grid[r][c] = '0'
        stack.append([r+1, c])
        stack.append([r-1, c])
        stack.append([r, c+1])
        stack.append([r, c-1])

def numIslands(grid):
    if not grid:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                count += 1
                dfs(grid, i, j, rows, cols)
    return count

if __name__ == "__main__":
    grid = [
    ['1','1','0','0','0'],
    ['1','1','0','0','0'],
    ['0','0','0','0','0'],
    ['0','0','1','1','1'],
    ['0','0','1','1','1']
]

    print("Number of islands:", numIslands(grid))
