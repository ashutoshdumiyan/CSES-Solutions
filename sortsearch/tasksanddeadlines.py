from sys import stdin

n = int(stdin.readline())

grid = []
for i in range(n):
    a, d = map(int, stdin.readline().split())
    grid.append([a, d])

grid.sort()

x = 0
y = 0

for i in range(n):
    x += grid[i][0]
    y += grid[i][1] - x

print(y)
