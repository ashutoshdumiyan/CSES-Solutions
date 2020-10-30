from sys import stdin

n = int(stdin.readline())
li = [int(c) for c in stdin.readline().split()]
s = sum(li)
p = (n * (n + 1)) // 2
print(p - s)
