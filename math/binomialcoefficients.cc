#include <bits/stdc++.h>
using namespace std;
#define ll long long int
const ll mod = 1000000007;
ll fact[1000001];

ll modinv(ll num)
{
    ll res = 1;
    ll b = mod - 2;

    while (b)
    {
        if (b & 1)
        {
            res = (res % mod * num % mod) % mod;
            b -= 1;
        }
        else
        {
            num = (num % mod * num % mod) % mod;
            b = b / 2;
        }
    }
    return res;
}

ll binomial(ll a, ll b)
{
    ll res = fact[a];
    res = (res % mod * modinv(fact[b]) % mod) % mod;
    res = (res % mod * modinv(fact[a - b]) % mod) % mod;
    return res;
}

int main()
{
    ll n;
    cin >> n;
    fact[0] = 1;
    for (ll i = 1; i <= 1000000; i++)
    {
        fact[i] = (i % mod * fact[i - 1] % mod) % mod;
    }
    while (n--)
    {
        ll a, b;
        cin >> a >> b;
        cout << binomial(a, b) << '\n';
    }
}