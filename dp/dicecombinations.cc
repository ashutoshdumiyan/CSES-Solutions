#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    int mod = 1000000007;
    cin >> n;
    vector<int> dp(n + 1, 0);
    dp[0] = 1;
    for (int i = 1; i <= n; i++)
    {
        int j = 1;
        while (j <= 6 && i - j >= 0)
        {
            dp[i] = (dp[i] % mod + dp[i - j] % mod) % mod;
            j += 1;
        }
    }
    cout << dp[n];
    return 0;
}