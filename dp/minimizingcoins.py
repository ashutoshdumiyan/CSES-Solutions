from sys import stdin

n, amount = map(int, stdin.readline().split())
coins = [int(c) for c in stdin.readline().split()]

infi = 10 ** 9
dp = [infi] * (amount + 1)
dp[0] = 0

for i in range(1, amount + 1):
    ans = infi
    for j in range(n):
        if coins[j] <= i:
            ans = min(ans, dp[i - coins[j]])
    if ans == infi:
        dp[i] = infi
    else:
        dp[i] = ans + 1
if dp[amount] == infi:
    print(-1)
else:
    print(dp[amount])
