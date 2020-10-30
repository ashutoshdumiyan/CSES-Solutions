from sys import stdin
from heapq import heapify, heappop, heappush
from bisect import insort_left

n, k = map(int, stdin.readline().split())
li = [int(c) for c in stdin.readline().split()]

# lower = []
# higher = []

window = li[:k]
window.sort()
print(window)

ans = window[k // 2] if k % 2 == 1 else window[k // 2 - 1]
print(ans, end=" ")

for i in range(k, n):
    window.pop(0)
    insort_left(window, li[i])
    print(window)
    median = window[k // 2] if k % 2 == 1 else window[k // 2 - 1]
    print(median, end=" ")
