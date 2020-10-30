from sys import stdin
from bisect import bisect, bisect_left, bisect_right

n, m = map(int, stdin.readline().split())

a = [int(c) for c in stdin.readline().split()]
b = [int(c) for c in stdin.readline().split()]

a.sort()

for i in range(m):
    t = bisect_right(a, b[i])
    print(a[t - 1])
    a.pop(t - 1)
