from sys import stdin

mod = 1000000007
fact = [0] * 1000001
fact[0] = 1
for o in range(2, 1000001):
    fact[o] = ((o - 1) * fact[o - 1] + (o - 1) * fact[o - 2]) % mod


n = int(input())
print(fact[n])
