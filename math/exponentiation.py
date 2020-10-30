from sys import stdin
mod = 10 ** 9 + 7


def power(a, b):
    res = 1

    while b:
        if b & 1:
            res = (res % mod * a % mod) % mod
            b -= 1
        else:
            a = (a % mod * a % mod) % mod
            b = b // 2
    return res


t = int(stdin.readline())
for _ in range(t):
    a, b = map(int, stdin.readline().split())
    print(power(a, b))
