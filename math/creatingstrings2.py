from collections import defaultdict
from threading import Thread

mod = 1000000007
fact = [0] * 1000001
fact[0] = 1
for o in range(1, 1000001):
    fact[o] = (o % mod * fact[o - 1 % mod]) % mod


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


def main():
    s = input()
    n = len(s)
    d = defaultdict(int)
    res = fact[n]
    for i in s:
        d[i] += 1
    for j in d:
        res = (res % mod * modinv(fact[d[j]]) % mod) % mod
    print(res)


Thread(target=main).start()
