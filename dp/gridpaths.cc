#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int mod = 1e9 + 7;
    vector<vector<int>> dp(n, vector<int>(n, 0));
    dp[0][0] = 1;
    for (int i = 0; i < n; i++)
    {
        string row;
        cin >> row;
        for (int j = 0; j < n; j++)
        {
            if (row[j] == '*')
            {
                dp[i][j] = 0;
            }
            else
            {
                if (i > 0)
                {
                    (dp[i][j] += dp[i - 1][j]) %= mod;
                }
                if (j > 0)
                {
                    (dp[i][j] += dp[i][j - 1]) %= mod;
                }
            }
        }
    }
    cout << dp[n - 1][n - 1];
    return 0;
}