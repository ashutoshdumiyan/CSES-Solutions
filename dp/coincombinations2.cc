#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, x;
    cin >> n >> x;
    int mod = 1e9 + 7;
    vector<int> li(n);
    for (int o = 0; o < n; o++)
        cin >> li[o];
    vector<int> dp(x + 1, 0);
    dp[0] = 1;
    for (int i = 0; i < n; i++)
    {
        for (int j = li[i]; j <= x; j++)
        {
            (dp[j] += dp[j - li[i]]) %= mod;
        }
    }
    cout << dp[x];
    return 0;
}