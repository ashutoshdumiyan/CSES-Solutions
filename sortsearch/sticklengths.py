from sys import stdin

n = int(stdin.readline())
li = [int(c) for c in stdin.readline().split()]

li.sort()

median = li[n // 2]
res = 0

for i in range(n):
    res += abs(li[i] - median)

print(res)
