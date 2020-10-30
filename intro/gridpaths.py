from sys import setrecursionlimit

setrecursionlimit(10 ** 6)


def isValid(x, y, visited):
    if x < 0 or x >= 7 or y < 0 or y >= 7:
        return False
    if visited[x][y] == True:
        return False
    return True


def ans(grid, visited, x, y):
    res = []
    visited[x][y] = True

    if isValid(x - 1, y, visited):
        res.append("U")
        res += ans(grid, visited, x - 1, y)
    if isValid(x, y + 1, visited):
        res.append("R")
        res += ans(grid, visited, x, y + 1)
    if isValid(x + 1, y, visited):
        res.append("D")
        res += ans(grid, visited, x + 1, y)
    if isValid(x, y - 1, visited):
        res.append("L")
        res += ans(grid, visited, x, y - 1)
    # visited[x][y] = False
    return res


s = input()
grid = [[0] * 7 for _ in range(7)]
visited = [[0] * 7 for _ in range(7)]
paths = ans(grid, visited, 0, 0)
print(len(paths))
print(paths)
