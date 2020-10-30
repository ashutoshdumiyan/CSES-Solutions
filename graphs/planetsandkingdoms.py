# Check Strongly connected graph
# kosaraju algorithm

from sys import stdin, setrecursionlimit, exit
from collections import defaultdict, deque

setrecursionlimit(10 ** 6)


def StackFillingDFS(start, graph, visited, stack):
    visited[start] = True

    for node in graph[start]:
        if not visited[node]:
            StackFillingDFS(node, graph, visited, stack)
    stack.append(start)


def dfs(start, graph, visited, result, count):
    result[start] = count
    visited[start] = True
    for node in graph[start]:
        if not visited[node]:
            dfs(node, graph, visited, result, count)


v, e = map(int, stdin.readline().split())
graph = defaultdict(list)
grapht = defaultdict(list)
visited = [0] * (v + 1)
stack = deque()
for i in range(e):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    grapht[b].append(a)

count = 1

for u in range(1, v + 1):
    if not visited[u]:
        StackFillingDFS(u, graph, visited, stack)
result = [-1] * (v + 1)

for j in range(1, v + 1):
    if not visited[j]:
        # print(j, end=" ")
        result[j] = count
        count += 1


visited = [0] * (v + 1)
while len(stack):
    node = stack.pop()
    if not visited[node]:
        dfs(node, grapht, visited, result, count)
        count += 1
print(count - 1)
# print(result)
for i in range(1, v + 1):
    print(result[i], end=" ")
