from sys import stdin
from collections import defaultdict, deque
from threading import Thread


def bfs(t, graph, visited):
    visited[t] = True
    # parent[t] = -1
    q = deque()
    q.append(t)

    clen = 0
    st = set()
    while len(q) > 0:
        node = q.popleft()
        st.add(node)
        clen += 1

        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
            else:
                # print(clen, node)
                print(clen, node, st)
                clen = 0


def main():
    n = int(stdin.readline())
    graph = defaultdict(list)
    i = 1
    for u in stdin.readline().split():
        graph[i].append(int(u))
        i += 1
    visited = [False] * (n + 1)
    # parent = [-1] * (n + 1)
    # bfs(5, graph, visited)
    # print("abc")
    for t in range(1, n + 1):
        if not visited[t]:
            st = bfs(t, graph, visited)
    print(visited)


Thread(target=main).start()
