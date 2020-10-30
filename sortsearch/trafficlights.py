from sys import stdin
from bisect import bisect

x, n = map(int, stdin.readline().split())
li = [int(c) for c in stdin.readline().split()]
res = [0, x]
count = 0

for i in range(n):
    t = bisect(res, li[i])
    print(t)
    # print(res[t - 1], res[t + 1])
    res.append(li[i])
    res.sort()
