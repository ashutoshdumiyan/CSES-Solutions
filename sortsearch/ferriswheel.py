from sys import stdin

n, x = map(int, stdin.readline().split())
li = [int(c) for c in stdin.readline().split()]
li.sort()
res = 0

i = 0
j = n - 1

while i <= j:
    if li[i] + li[j] > x:
        j -= 1
    else:
        i += 1
        j -= 1
    res += 1

print(res)
