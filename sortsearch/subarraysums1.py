from sys import stdin
from collections import defaultdict

n, k = map(int, stdin.readline().split())
li = [int(c) for c in stdin.readline().split()]
prevsum = defaultdict(int)

res = 0
currsum = 0

for i in range(n):
    currsum += li[i]

    if currsum == k:
        res += 1

    if currsum - k in prevsum:
        res += prevsum[currsum - k]

    prevsum[currsum] += 1

print(res)
