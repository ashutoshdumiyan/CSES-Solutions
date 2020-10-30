#include <bits/stdc++.h>
using namespace std;
#define ll long long int

const int mod = 1000000007;

ll divisorsum(ll num)
{
    ll i = 1;
    ll res = 0;

    while (i * i <= num)
    {
        if (num % i == 0)
        {
            if (num / i == i)
            {
                res = (res % mod + i % mod) % mod;
            }
            else
            {
                res = (res % mod + i % mod + (num / i) % mod) % mod;
            }
        }
        i += 1;
    }
    cout << '\n';
    return res;
}

int main()
{
    ll n;
    cin >> n;
    ll res = 0;
    for (int i = 1; i <= n; i++)
        res += divisorsum(i);
    cout << res;
    return 0;
}