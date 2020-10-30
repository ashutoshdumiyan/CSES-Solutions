from sys import stdin, stdout, maxsize
from collections import defaultdict


def main():
    v, e = map(int, stdin.readline().split())
    graph = defaultdict(list)
    dist = []
    for i in range(e):
        a, b, w = map(int, stdin.readline().split())
        graph[a].append([b, w])
    dist = [-maxsize] * (v + 1)
    dist[1] = 0
    for u in range(v - 1):
        for j in range(1, v + 1):
            for node, cost in graph[j]:
                if dist[j] + cost > dist[node]:
                    dist[node] = dist[j] + cost
    print(dist[v])


if __name__ == "__main__":
    main()
