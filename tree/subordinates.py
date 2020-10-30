from sys import stdin, setrecursionlimit
from collections import defaultdict

setrecursionlimit(10 ** 6)


def dfs(start, tree, visited, res):
    visited[start] = True
    count = 1

    for node in tree[start]:
        if not visited[node]:
            count += dfs(node, tree, visited, res)
    res[start] = count
    return count


def main():
    n = int(stdin.readline())
    li = [int(c) for c in stdin.readline().split()]
    tree = defaultdict(list)
    for i in range(1, n):
        tree[li[i - 1]].append(i + 1)
    visited = [False] * (n + 1)
    res = [0] * (n + 1)
    for u in range(1, n + 1):
        if not visited[u]:
            dfs(u, tree, visited, res)
    for u in range(1, n + 1):
        print(res[u] - 1, end=" ")


if __name__ == "__main__":
    main()
