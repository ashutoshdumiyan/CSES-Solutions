from sys import stdin

n = int(stdin.readline())

for i in range(1, n + 1):
    res = 0
    t = i * i
    # add C(t, 2) to res
    res += (t * (t - 1)) // 2
    if i > 2:
        # Write the cases manually and see the pattern
        res -= 4 * (i - 1) * (i - 2)
    print(res)
