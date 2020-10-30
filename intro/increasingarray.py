from sys import stdin

n = int(stdin.readline())
li = [int(c) for c in stdin.readline().split()]
res = 0

for i in range(1, n):
    if li[i] < li[i - 1]:
        res += li[i - 1] - li[i]
        li[i] = li[i - 1]
print(res)
