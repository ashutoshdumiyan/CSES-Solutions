from sys import stdin
# Longest Increasing subsequence
from bisect import bisect_right

n = int(stdin.readline())
li = [int(c) for c in stdin.readline().split()]

res = []

for i in range(n):
    pos = bisect_right(res, li[i])
    if pos >= len(res):
        res.append(li[i])
    else:
        res[pos] = li[i]
    print(res)

print(len(res))
