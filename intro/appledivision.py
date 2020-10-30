from sys import stdin, maxsize

n = int(stdin.readline())
li = [int(c) for c in stdin.readline().split()]
s = sum(li)
res = 0

for i in range(1 << n):
    temp = 0
    for j in range(n):
        if (i >> j) & 1:
            temp += li[j]
    if temp <= s / 2:
        res = max(res, temp)
print(s - 2 * res)
