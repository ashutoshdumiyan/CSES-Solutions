from sys import stdin, stdout, setrecursionlimit
from collections import defaultdict

# Done

setrecursionlimit(10 ** 6)


def dfs(start):
    global visited
    visited[start] = True

    for node in graph[start]:
        if not visited[node]:
            dfs(node)


graph = defaultdict(list)
v, e = [int(c) for c in stdin.readline().split()]
visited = [False] * (v + 1)
for i in range(e):
    a, b = [int(c) for c in stdin.readline().split()]
    graph[a].append(b)
    graph[b].append(a)
count = -1
res = ""
prev = -1
for i in range(1, v + 1):
    if not visited[i]:
        if prev != -1:
            res += str(prev) + " " + str(i) + "\n"
        prev = i
        count += 1
        dfs(i)
print(count)
stdout.write(res)
