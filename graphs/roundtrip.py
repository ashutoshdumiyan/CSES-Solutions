from sys import stdin, stdout, exit, setrecursionlimit
from collections import defaultdict, deque

# Done
# Print a cycle when it's first encountered by storing parent of traversed nodes

setrecursionlimit(10 ** 6)


def dfs(start, graph, visited, parent, pr):
    visited[start] = True
    parent[start] = pr

    for node in graph[start]:
        if node == parent[start]:
            continue
        if not visited[node]:
            dfs(node, graph, visited, parent, start)
        else:
            tp = start
            res = deque()
            while tp != parent[node]:
                res.append(tp)
                tp = parent[tp]
            res.append(start)
            print(len(res))
            while len(res) > 0:
                print(res.popleft(), end=" ")
            exit(0)


def main():
    v, e = map(int, stdin.readline().split())
    graph = defaultdict(list)
    for i in range(e):
        a, b = map(int, stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (v + 1)
    tin = [0] * (v + 1)
    parent = [-1] * (v + 1)
    for j in range(1, v + 1):
        if not visited[j]:
            dfs(j, graph, visited, parent, -1)
    stdout.write("IMPOSSIBLE\n")


if __name__ == "__main__":
    main()
