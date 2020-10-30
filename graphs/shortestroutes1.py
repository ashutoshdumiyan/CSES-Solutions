from sys import stdin, stdout, maxsize
from collections import defaultdict
from heapq import heapify, heappush, heappop

# T.L.E in one test case


def main():
    v, e = map(int, stdin.readline().split())
    graph = defaultdict(list)
    for i in range(e):
        a, b, w = map(int, stdin.readline().split())
        graph[a].append([b, w])
    dist = [maxsize] * (v + 1)
    dist[1] = 0
    q = []
    heapify(q)
    heappush(q, [0, 1])

    while len(q) > 0:
        curr_d, curr = heappop(q)

        if curr_d > dist[curr]:
            continue

        for x in graph[curr]:
            if curr_d + x[1] < dist[x[0]]:
                dist[x[0]] = curr_d + x[1]
                heappush(q, [dist[x[0]], x[0]])
    for o in range(1, v + 1):
        print(dist[o], end=" ")
    # stdout.write(" ".join(dist[1:]))


if __name__ == "__main__":
    main()
