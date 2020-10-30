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
    return res % mod


n = int(input())
s = input()
k = len(s)
t = n - k + 1
print(t * (power(26, (t - 1))))
