from sys import stdin

n = int(stdin.readline())
li = [int(c) for c in stdin.readline().split()]
s = set()
for i in li:
    s.add(i)
print(len(s))
