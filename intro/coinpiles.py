from sys import stdin

for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    if (a + b) % 3 == 0 and min(a, b) * 2 >= max(a, b):
        print("YES")
    else:
        print("NO")
