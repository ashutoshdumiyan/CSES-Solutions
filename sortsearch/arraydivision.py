from threading import Thread
from sys import stdin


def split(li, mid):
    pieces = 1
    tempSum = 0
    for i in li:
        if tempSum + i > mid:
            pieces += 1
            tempSum = i
        else:
            tempSum += i
    return pieces


def main():
    n, k = map(int, stdin.readline().split())
    li = [int(c) for c in stdin.readline().split()]

    mx = 0
    s = 0
    for i in range(n):
        if li[i] > mx:
            mx = li[i]
        s += li[i]

    lo = mx
    hi = s

    while lo < hi:
        mid = (lo + hi) // 2
        pieces = split(li, mid)
        if pieces > k:
            lo = mid + 1
        else:
            hi = mid

    print(lo)


Thread(target=main).start()
