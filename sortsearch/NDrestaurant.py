from sys import stdin

n = int(stdin.readline())

grid = []

for i in range(n):
    a, b = map(int, stdin.readline().split())
    grid.append([a, b])

grid.sort(key=lambda x: x[1])
# print(grid)

res = 0
last = 0

for u in range(n):
    # print(last, grid[u][0])
    if last == 0:
        res += 1
        last = grid[u][1]
    elif grid[u][0] <= last:
        res += 1
        last = grid[u][1]
print(res)
