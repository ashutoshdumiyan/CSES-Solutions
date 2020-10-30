from sys import stdin, maxsize
from collections import defaultdict
from heapq import heapify, heappush, heappop
from threading import Thread


def solve(u, graph, dist, v):
    dist[u] = 0
    q = []
    heapify(q)
    heappush(q, [0, u])

    while len(q) > 0:
        curr_d, curr = heappop(q)

        if curr_d > dist[curr]:
            continue

        if curr == v:
            break

        for node, cost in graph[curr]:
            if curr_d + cost < dist[node]:
                dist[node] = curr_d + cost
                heappush(q, [dist[node], node])


def main():
    v, e = map(int, stdin.readline().split())
    graph1 = defaultdict(list)
    graph2 = defaultdict(list)
    for i in range(e):
        a, b, w = map(int, stdin.readline().split())
        graph1[a].append([b, w])
        graph2[b].append([a, w])
    dist1 = [maxsize] * (v + 1)
    dist2 = [maxsize] * (v + 1)
    solve(1, graph1, dist1, v)
    solve(v, graph2, dist2, 1)
    ans = maxsize
    for t in range(1, v + 1):
        for r in graph1[t]:
            ans = min(ans, dist1[t] + dist2[r[0]] + r[1] // 2)
    print(ans)


Thread(target=main).start()
