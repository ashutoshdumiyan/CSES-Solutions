from sys import stdin

n = int(stdin.readline())
grid = []
for i in range(n):
    a, b = map(int, stdin.readline().split())
    grid.append([a, b])

grid.sort(key=lambda x: x[1])

print(grid)
