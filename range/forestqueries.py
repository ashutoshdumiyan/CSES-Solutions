from sys import stdin

n, q = map(int, stdin.readline().split())
grid = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    temp = []
    t = input()
    for j in range(1, n + 1):
        if t[j - 1] == '.':
            grid[i][j] = 0
        else:
            grid[i][j] = 1


dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = dp[0][1] = dp[1][0] = 0
# dp[i][j] = number of trees until index i, j (top and left and topleft and current)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = grid[i][j] + dp[i - 1][j] + dp[i][j - 1] + dp[i - 1][j - 1]


for _ in range(q):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    print(dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1])
