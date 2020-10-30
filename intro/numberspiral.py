from sys import stdin

for _ in range(int(stdin.readline())):
    y, x = map(int, stdin.readline().split())
    tp = max(x, y)
    ans = (tp - 1) ** 2
    if tp % 2:
        if y == tp:
            ans += x
        else:
            ans += 2 * tp - y
    else:
        if x == tp:
            ans += y
        else:
            ans += 2 * tp - x
    print(ans)
