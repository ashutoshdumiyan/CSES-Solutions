from sys import stdin

n = int(stdin.readline())
mod = 10 ** 9 + 7
dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n + 1):
    j = 1
    while j <= 6 and i - j >= 0:
        dp[i] = (dp[i] % mod + dp[i - j] % mod) % mod
        j += 1
print(dp[n])
