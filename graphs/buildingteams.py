from sys import stdin, stdout
from collections import defaultdict, deque


def bfs(start, graph, visited, badges):
    q = deque()
    q.append([start, 1])
    visited[start] = True
    badges[start] = 1

    flag = True

    while len(q) > 0:
        node, tag = q.popleft()

        for nbr in graph[node]:
            if not visited[nbr]:
                badges[nbr] = badges[node] % 2 + 1
                visited[nbr] = True
                q.append([nbr, badges[nbr]])
            else:
                if badges[nbr] == badges[node]:
                    flag = False
                    return flag
    return flag


def main():
    v, e = map(int, stdin.readline().split())
    graph = defaultdict(list)
    for i in range(e):
        a, b = map(int, stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (v + 1)
    badges = [0] * (v + 1)
    fl = True
    for i in range(1, v + 1):
        if not visited[i]:
            temp = bfs(i, graph, visited, badges)
            if not temp:
                fl = False
                break
    if fl:
        for o in range(1, v + 1):
            stdout.write(str(badges[o]) + " ")
        stdout.write("\n")
    else:
        stdout.write("IMPOSSIBLE\n")


if __name__ == "__main__":
    main()
