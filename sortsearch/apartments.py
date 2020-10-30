from sys import stdin

n, m, k = map(int, stdin.readline().split())

des = [int(c) for c in stdin.readline().split()]
ava = [int(c) for c in stdin.readline().split()]

des.sort()
ava.sort()

count = 0

i = 0
j = 0

while i < n and j < m:
    if des[i] + k < ava[j]:
        i += 1
    elif des[i] - k > ava[j]:
        j += 1
    else:
        i += 1
        j += 1
        count += 1

print(count)
