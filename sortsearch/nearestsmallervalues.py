from sys import stdin
from collections import deque
from bisect import bisect

n = int(stdin.readline())
li = [int(c) for c in stdin.readline().split()]

S = deque()

# Traverse all array elements
for i in range(n):
    while (len(S) > 0 and S[-1][0] >= li[i]):
        S.pop()
    if (len(S) == 0):
        print("0", end=" ")
    else:
        print(S[-1][1] + 1, end=" ")
    S.append([li[i], i])
