from sys import stdin

n, q = map(int, stdin.readline().split())
li = [int(c) for c in stdin.readline().split()]
prefix = [0] * n
prefix[0] = li[0]
for i in range(1, n):
    prefix[i] += prefix[i - 1] + li[i]

for u in range(q):
    a, b = map(int, stdin.readline().split())
    b -= 1
    a -= 1
    if a == 0:
        print(prefix[b])
    else:
        print(prefix[b] - prefix[a - 1])
