from sys import stdin

mod = 1000000007
fact = [0] * 2000002
fact[0] = 1
for o in range(1, 2000002):
    fact[o] = (fact[o - 1] % mod * o % mod) % mod


def modinv(num):
    res = 1
    b = mod - 2
    while b:
        if b & 1:
            res = (res % mod * num % mod) % mod
            b -= 1
        else:
            num = (num % mod * num % mod) % mod
            b = b // 2
    return res


def printAns(n, m):
    rs = fact[n + m - 1]
    rs = (rs % mod * modinv(fact[n - 1]) % mod) % mod
    rs = (rs % mod * modinv(fact[m]) % mod) % mod
    return rs


n, m = map(int, stdin.readline().split())
print(printAns(n, m))
