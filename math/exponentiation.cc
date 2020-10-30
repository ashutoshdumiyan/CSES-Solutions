#include <bits/stdc++.h>
using namespace std;
#define ll long long int

const int mod = 1000000007;

ll power(ll a, ll b)
{
    ll res = 1;
    while (b)
    {
        if (b & 1)
        {
            res = (res % mod * a % mod) % mod;
            b -= 1;
        }
        else
        {
            a = (a % mod * a % mod) % mod;
            b = b / 2;
        }
    }
    return res;
}

int main()
{
    int n;
    cin >> n;
    while (n--)
    {
        ll a, b;
        cin >> a >> b;
        cout << power(a, b) << '\n';
    }
    return 0;
}