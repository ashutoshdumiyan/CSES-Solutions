from sys import stdin, stdout, maxsize
from collections import defaultdict, deque
from threading import Thread


def main():
    v, e = map(int, stdin.readline().split())
    graph = defaultdict(list)
    dist = []
    for i in range(e):
        a, b, w = map(int, stdin.readline().split())
        graph[a].append([b, w])
    dist = [maxsize] * (v + 1)
    parent = [-1] * (v + 1)
    dist[1] = 0
    res = []
    x = None
    for j in range(1, v + 1):
        x = -1
        for node, cost in graph[j]:
            if dist[j] + cost < dist[node]:
                dist[node] = dist[j] + cost
                parent[node] = j
                x = node

    if x == -1:
        print("NO")
    else:
        for i in range(1, v + 1):
            x = parent[x]
        cycle = deque()
        f = x
        while True:
            cycle.append(f)
            if f == x and len(cycle) > 1:
                break
            f = parent[f]
        print("YES")
        while len(cycle):
            print(cycle.popleft(), end=" ")


Thread(target=main).start()
