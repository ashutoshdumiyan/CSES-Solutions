#include <bits/stdc++.h>
using namespace std;

int grid[1001][1001], dp[1001][1001];

int main()
{
    int n, q;
    cin >> n >> q;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            char ch;
            cin >> ch;
            if (ch == '*')
                grid[i][j] = 1;
            else
                grid[i][j] = 0;
        }
    }
    dp[0][0] = dp[1][0] = dp[0][1] = 0;

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
            dp[i][j] = grid[i][j] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1];
    }
    while (q--)
    {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        cout << dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1] << '\n';
    }
    return 0;
}