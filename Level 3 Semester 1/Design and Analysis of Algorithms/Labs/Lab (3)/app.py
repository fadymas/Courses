
"""import time
coins = [1, 2, 3]
total = 5
dp = [0] * (total + 1)
dp[0] = 1  # one way to make sum 0 (no coins)
start_time = time.time()
i = 0
while i < len(coins):
    coin = coins[i]
    j = coin
    while j <= total:
        dp[j] += dp[j - coin]
        j += 1
    i += 1
end_time = time.time()

print(f"Coins: {coins}")
print(f"Target Sum: {total}")
print(f"Total number of ways: {dp[total]}")
print(f"Execution time: {end_time - start_time:.6f} seconds")
"""

"""import time
n = 10
a = 0
b = 1
next = b
count = 1
start_time = time.time()
while count <= n:
    print(next, end=" ")
    count += 1
    a, b = b, next
    next = a + b
end_time = time.time()
print(f"\nExecution time: {end_time - start_time:.6f} seconds")
"""

"""import time
def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return b
    else:
        for _ in range(1, n):
            c = a + b
            a, b = b, c
        return b
start_time = time.time()
result = fibonacci(9)
end_time = time.time()
print(f"Result: {result}")
print(f"Execution time: {end_time - start_time:.6f} seconds")
"""



"""import time
N = 3
rods = {'A': list(range(N, 0, -1)), 'B': [], 'C': []}
def move_disk(from_rod, to_rod):
    disk = rods[from_rod].pop()
    rods[to_rod].append(disk)
    print(f"Move disk {disk} from rod {from_rod} to rod {to_rod}")
start_time = time.time()
if N % 2 == 0:
    dest, aux = 'B', 'C'
else:
    dest, aux = 'C', 'B'

total_moves = 2 ** N - 1
moves = 1
while moves <= total_moves:
    if moves % 3 == 1:
        if not rods['A'] or (rods[dest] and rods['A'][-1] > rods[dest][-1]):
            move_disk(dest, 'A')
        else:
            move_disk('A', dest)
    elif moves % 3 == 2:
        if not rods['A'] or (rods[aux] and rods['A'][-1] > rods[aux][-1]):
            move_disk(aux, 'A')
        else:
            move_disk('A', aux)
    elif moves % 3 == 0:
        if not rods[aux] or (rods[dest] and rods[aux][-1] > rods[dest][-1]):
            move_disk(dest, aux)
        else:
            move_disk(aux, dest)
    moves += 1
end_time = time.time()
print(f"\nTotal moves: {total_moves}")
print(f"Execution time: {end_time - start_time:.6f} seconds")"""