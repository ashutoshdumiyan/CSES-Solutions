from sys import stdin

n, t = map(int, stdin.readline().split())
li = [int(c) for c in stdin.readline().split()]

lb = 1
rb = 10 ** 18

while lb < rb:
    mb = (lb + rb) // 2
    s = 0
    for i in range(n):
        s += min(mb // li[i], 10 ** 9)
    if s >= t:
        rb = mb
    else:
        lb = mb + 1

print(lb)
