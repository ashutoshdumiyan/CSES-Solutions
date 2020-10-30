from sys import stdin, exit
from collections import defaultdict

n, k = map(int, stdin.readline().split())
li = [int(c) for c in stdin.readline().split()]
d = defaultdict(int)
for i in range(n):
    d[li[i]] = i

for j in range(n):
    if k - li[j] in d and d[k - li[j]] != j:
        print(j + 1, d[k - li[j]] + 1)
        exit(0)
print("IMPOSSIBLE")
