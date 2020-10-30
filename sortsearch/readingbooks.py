from sys import stdin

n = int(stdin.readline())
li = [int(c) for c in stdin.readline().split()]
li.sort()
s = sum(li)
print(max(s, 2 * li[n - 1]))
