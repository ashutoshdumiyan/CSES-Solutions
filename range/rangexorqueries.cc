#include <bits/stdc++.h>
using namespace std;
#define ll long long int

ll li[200001], st[800001];

void build(ll si, ll ss, ll se)
{
    if (ss == se)
    {
        st[si] = li[ss];
        return;
    }
    ll mid = (ss + se) / 2;
    build(2 * si, ss, mid);
    build(2 * si + 1, mid + 1, se);
    st[si] = st[2 * si] ^ st[2 * si + 1];
}

ll query(ll si, ll ss, ll se, ll qs, ll qe)
{
    if (ss > qe || se < qs)
    {
        return 0;
    }
    if (ss >= qs && se <= qe)
    {
        return st[si];
    }
    ll mid = (ss + se) / 2;
    ll l = query(2 * si, ss, mid, qs, qe);
    ll r = query(2 * si + 1, mid + 1, se, qs, qe);
    return l ^ r;
}

int main()
{
    int n, q;
    cin >> n >> q;
    for (int o = 1; o <= n; o++)
        cin >> li[o];
    build(1, 1, n);
    while (q--)
    {
        int a, b;
        cin >> a >> b;
        cout << query(1, 1, n, a, b) << '\n';
    }
    return 0;
}