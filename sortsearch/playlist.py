from sys import stdin
from collections import defaultdict

n = int(stdin.readline())
li = [int(c) for c in stdin.readline().split()]

d = defaultdict(int)

curr = 0
res = 0

for i in range(n):
    if li[i] not in d:
        curr += 1
        d[li[i]] = i
        res = max(res, curr)
    else:
        # d = defaultdict(int)
        del d[li[i]]
        d[li[i]] = i
        curr = len(d)
        res = max(res, curr)
        d = defaultdict(int)
    # print(d)

print(res)
