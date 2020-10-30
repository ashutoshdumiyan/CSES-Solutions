from sys import stdin
from collections import defaultdict

n = int(stdin.readline())
li = [int(c) for c in stdin.readline().split()]
d = defaultdict(int)

res = 0
currsum = 0

for i in range(n):
    currsum += li[i]

    if currsum % n == 0:
        res += 1

    if (currsum % n + n) % n in d:
        res += d[(currsum % n + n) % n]

    d[currsum % n] += 1

print(res)
