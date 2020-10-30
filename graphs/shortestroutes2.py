from sys import stdin, maxsize
from threading import Thread


def dotask(q, dist):
    for p in range(q):
        one, two = map(int, stdin.readline().split())
        temp = dist[one][two]
        print(-1 if temp >= maxsize else temp)


def main():
    v, e, q = map(int, stdin.readline().split())
    dist = [[maxsize] * (v + 1) for _ in range(v + 1)]
    for i in range(e):
        a, b, w = map(int, stdin.readline().split())
        dist[a][b] = min(dist[a][b], w)
        dist[b][a] = min(dist[b][a], w)

    for t in range(v + 1):
        dist[t][t] = 0

    for k in range(1, v + 1):
        for i in range(1, v + 1):
            for j in range(1, v + 1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    Thread(target=dotask, args=(q, dist)).start()


Thread(target=main).start()
