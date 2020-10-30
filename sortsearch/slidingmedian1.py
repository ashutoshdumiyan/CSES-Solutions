from sys import stdin
from heapq import heapify, heappop, heappush


def balance(left, right):
    L = len(left)
    R = len(right)
    while abs(L - R) > 1:
        if L < R:
            heappush(left, -1 * heappop(right))
        else:
            heappush(right, -1 * heappop(left))
        L = len(left)
        R = len(right)


def getmedian(left, right):
    L = len(left)
    R = len(right)

    if not L and not R:
        return 0

    if L >= R:
        return left[0] * -1
    elif R > L:
        return right[0]


def insert(left, right, num):
    med = getmedian(left, right)

    if num > med:
        if len(right) > len(left):
            heappush(left, -1 * heappop(right))
        heappush(right, num)
    else:
        if len(left) > len(right):
            heappush(right, -1 * heappop(left))
        heappush(left, num * -1)


def remove(left, right, num):
    if -1 * num in left:
        left.remove(-1 * num)
        heapify(left)
    else:
        right.remove(num)
        heapify(right)


n, k = map(int, stdin.readline().split())
li = [int(c) for c in stdin.readline().split()]

left = []
right = []

heapify(left)
heapify(right)

i = 0
while i < k:
    insert(left, right, li[i])
    i += 1

print(getmedian(left, right), end=" ")
while i < n:
    remove(left, right, li[i - k])
    balance(left, right)
    insert(left, right, li[i])
    print(getmedian(left, right), end=" ")
    i += 1
