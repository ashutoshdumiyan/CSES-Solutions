from sys import stdin, stdout
from collections import deque
from threading import Thread

# T.L.E

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def isValid(startx, starty, grid, visited):
    if startx < 0 or startx >= len(grid) or starty < 0 or starty >= len(grid[0]):
        return False
    if visited[startx][starty] or grid[startx][starty] == '#':
        return False
    return True


def bfs(startx, starty, endx, endy, grid, visited, parent):
    # global grid, visited, dist, parent
    # res = ""
    visited[startx][starty] = True
    # dist[startx][starty] = 0
    q = deque()
    q.append([startx, starty])
    # path = ""
    while len(q) > 0:
        currx, curry = q.popleft()
        # d = dist[currx][curry]
        if grid[currx][curry] == 'B':
            rs = ""
            xval = endx
            yval = endy
            count = 0
            while parent[xval][yval] != None:
                count += 1
                txval, tyval = parent[xval][yval]
                if txval > xval:
                    rs += "U"
                elif txval < xval:
                    rs += "D"
                elif tyval > yval:
                    rs += "L"
                elif tyval < yval:
                    rs += "R"
                xval = txval
                yval = tyval
            stdout.write("YES\n")
            print(count)
            # stdout.write(str(dist[endx][endy]) + "\n")
            stdout.write(rs[::-1])
            return

        for u in range(4):
            newx = currx + dx[u]
            newy = curry + dy[u]
            if isValid(newx, newy, grid, visited):
                parent[newx][newy] = [currx, curry]
                # path += dr
                visited[newx][newy] = True
                # dist[newx][newy] = d + 1
                # if grid[newx][newy] == 'B':
                #     return True
                q.append([newx, newy])
    print("NO")


def main():
    n, m = map(int, stdin.readline().split())
    grid = [0] * n
    visited = [0] * n
    # dist = [0] * n
    parent = [0] * n
    for i in range(n):
        li = list(stdin.readline())
        li.pop()
        grid[i] = li
        visited[i] = [False] * m
        # dist[i] = [0] * m
        parent[i] = [0] * m
    for j in range(n):
        for k in range(m):
            if grid[j][k] == 'A':
                parent[j][k] = None
                startx = j
                starty = k
            elif grid[j][k] == 'B':
                endx = j
                endy = k
    bfs(startx, starty, endx, endy, grid, visited, parent)


Thread(target=main).start()
