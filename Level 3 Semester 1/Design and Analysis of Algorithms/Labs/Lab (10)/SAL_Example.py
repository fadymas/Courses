def minDiceThrows(board):
    N = len(board)
    visited = []
    for i in range(N):
        visited.append(False)
    
    queue = []
    front = 0
    queue.append([0, 0])
    visited[0] = True
    
    while front < len(queue):
        curr, moves = queue[front]
        front += 1
        
        if curr == N - 1:
            return moves
        
        for i in range(1, 7):
            next_cell = curr + i
            if next_cell < N and not visited[next_cell]:
                visited[next_cell] = True
                dest = board[next_cell] if board[next_cell] != -1 else next_cell
                queue.append([dest, moves + 1])
    
    return -1

if __name__ == "__main__":
    N = 30
    board = []
    for i in range(N):
        board.append(-1)
    
    board[2] = 21
    board[4] = 7
    board[10] = 25
    board[19] = 28
    
    board[26] = 0
    board[20] = 8
    board[16] = 3
    board[18] = 6
    
    print("Minimum dice throws required:", minDiceThrows(board))
