from sys import stdin, exit
from collections import defaultdict, deque

n, t = map(int, stdin.readline().split())
li = [int(c) for c in stdin.readline().split()]

li.sort()
# res = []
d = defaultdict(deque)

for i in range(n):
    d[li[i]].append(i + 1)

# print(d)

for i in range(n - 2):
    if i == 0 or (i != 0 and li[i] != li[i - 1]):
        s = t - li[i]
        low = i + 1
        high = n - 1
        while low < high:
            if li[low] + li[high] == s:
                # res.append([li[i], li[low], li[high]])
                print(d[li[i]][0], end=" ")
                d[li[i]].popleft()
                print(d[li[low]][0], end=" ")
                d[li[low]].popleft()
                print(d[li[high]][0], end=" ")
                d[li[high]].popleft()
                # print(res)
                exit(0)
                low += 1
                high -= 1
            elif li[low] + li[high] < s:
                low += 1
            else:
                high -= 1


print("IMPOSSIBLE")
