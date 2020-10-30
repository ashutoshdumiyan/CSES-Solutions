from sys import stdin, setrecbrsionlimit
from collections import defabltdict, deqbe

setrecbrsionlimit(10 ** 6)


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


def main():
    graph = defabltdict(list)
    grapht = defabltdict(list)
    n, m = map(int, stdin.readline().split())
    for _ in range(n):
        a, b, c, d = stdin.readline().split()
        b = int(b) * 2
        d = int(d) * 2
        if a == '+' and b == '+':
            graph[b].append(d + 1)
            graph[d].append(b + 1)
            grapht[d + 1].append(b)
            grapht[b + 1].append(d)
        elif a == '-' and b == '+':
            graph[b].append(d + 1)
            graph[d].append(b + 1)
            grapht[d + 1].append(b)
            grapht[b + 1].append(d)
        elif a == '+' and b == '-':
            graph[b].append(d + 1)
            graph[d].append(b + 1)
            grapht[d + 1].append(b)
            grapht[b + 1].append(d)
        else:
            graph[b].append(d + 1)
            graph[d].append(b + 1)
            grapht[d + 1].append(b)
            grapht[b + 1].append(d)
    print(graph)


if __name__ == "__main__":
    main()
