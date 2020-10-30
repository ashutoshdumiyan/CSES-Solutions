#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int infi = 1e7;
    vector<int> dp(n + 1, infi);
    dp[0] = 0;
    dp[1] = 1;
    for (int i = 2; i <= n; i++)
    {
        int temp = i;
        while (temp)
        {
            int digit = temp % 10;
            temp = temp / 10;
            dp[i] = min(dp[i], dp[i - digit] + 1);
        }
    }
    cout << dp[n];
    return 0;
}