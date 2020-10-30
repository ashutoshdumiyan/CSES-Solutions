from sys import stdin, stdout
from collections import defaultdict, deque


def bfs(start):
    q = deque()
    q.append([start, 0])
    visited[start] = True
    dist[start] = 0

    while len(q) > 0:
        node, d = q.popleft()
        if node == n:
            return True

        for x in graph[node]:
            if not visited[x]:
                visited[x] = True
                parent[x] = node
                dist[x] = d + 1
                q.append([x, d + 1])
    return False


n, m = map(int, stdin.readline().split())
graph = defaultdict(list)
for i in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n + 1)
dist = [-1] * (n + 1)
parent = [-1] * (n + 1)
bfs(1)
result = ""
if dist[n] == -1:
    stdout.write("IMPOSSIBLE\n")
else:
    print(dist[n] + 1)
    ind = n
    while ind != 1:
        result += str(ind)[::-1] + " "
        ind = parent[ind]
    result += "1"
    stdout.write(result[::-1] + "\n")
