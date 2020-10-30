#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, x;
    cin >> n >> x;
    int li[n];
    for (int i = 0; i < n; i++)
        cin >> li[i];
    int infi = 10000000;
    vector<int> dp(x + 1, infi);
    dp[0] = 0;

    for (int j = 1; j <= x; j++)
    {

        int ans = infi;

        for (int k = 0; k < n; k++)
        {

            if (li[k] <= j)
            {
                ans = min(ans, dp[j - li[k]]);
            }
        }

        if (ans == infi)
        {
            dp[j] = infi;
        }
        else
        {
            dp[j] = ans + 1;
        }
    }
    if (dp[x] == infi)
        cout << -1;
    else
        cout << dp[x];
    return 0;
}