from sys import stdin, stdout, setrecursionlimit
from threading import Thread, stack_size

# T.L.E

setrecursionlimit(10 ** 6)
stack_size(2 ** 28)


def dfs(x, y, n, m, grid, visited):
    if x >= n or x < 0 or y >= m or y < 0:
        return
    if visited[x][y] or grid[x][y] == "#":
        return
    visited[x][y] = True

    dfs(x - 1, y, n, m, grid, visited)

    dfs(x, y + 1, n, m, grid, visited)

    dfs(x + 1, y, n, m, grid, visited)

    dfs(x, y - 1, n, m, grid, visited)


def main():
    n, m = map(int, stdin.readline().split())
    grid = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    i = 0
    while i < n:
        li = stdin.readline().split()
        for o in range(m):
            grid[i][o] = li[0][o]
        i += 1
    count = 0

    for j in range(n):
        for k in range(m):
            if visited[j][k] == False and grid[j][k] == ".":
                count += 1
                dfs(j, k, n, m, grid, visited)
    stdout.write(str(count) + "\n")


Thread(target=main).start()
