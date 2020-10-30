from sys import stdin
from collections import defaultdict, deque


def bfs(start, tree):
    visited = [False] * (len(tree) + 1)
    q = deque()
    level = 0
    q.append([start, level])
    visited[start] = True
    res = []
    while len(q):
        node = q.popleft()
        res = node
        visited[node[0]] = True
        level = node[1]
        for temp in tree[node[0]]:
            if not visited[temp]:
                q.append([temp, level + 1])
    return res


def main():
    n = int(stdin.readline())
    if n == 1:
        print(0)
    else:
        tree = defaultdict(list)
        for _ in range(n - 1):
            a, b = map(int, stdin.readline().split())
            tree[a].append(b)
            tree[b].append(a)
        first = bfs(1, tree)
        print(bfs(first[0], tree)[1])


if __name__ == "__main__":
    main()
