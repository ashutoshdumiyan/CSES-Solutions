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


def dfs(start, graph, visited):
    visited[start] = True
    # print(start, end=" ")
    for node in graph[start]:
        if not visited[node]:
            dfs(node, graph, visited)


v, e = map(int, stdin.readline().split())
graph = defaultdict(list)
grapht = defaultdict(list)
visited = [0] * (v + 1)
stack = deque()
for i in range(e):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    grapht[b].append(a)


StackFillingDFS(1, graph, visited, stack)
first = None
second = None
count = 0

for i in range(1, v + 1):
    if not visited[i]:
        print("NO")
        print(stack[-1], i)
        exit(0)

visited = [0] * (v + 1)
while len(stack):
    node = stack.pop()
    if not visited[node]:
        count += 1
        if not first:
            first = node
        second = node
        dfs(node, grapht, visited)
        # print()

if count > 1:
    print("NO")
    print(second, first)
else:
    print("YES")
