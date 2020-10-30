#include <bits/stdc++.h>
using namespace std;
#define ll long long int

ll li[200001], st[800001], lazy[800001];

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
    st[si] = st[2 * si] + st[2 * si + 1];
}

ll query(ll si, ll ss, ll se, ll qs, ll qe)
{
    if (lazy[si] != 0)
    {
        ll dx = lazy[si];
        lazy[si] = 0;
        st[si] += dx * (se - ss + 1);
        if (ss != se)
            lazy[2 * si] += dx, lazy[2 * si + 1] += dx;
    }

    if (se < qs || ss > qe)
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
    return l + r;
}

// Lazy propagration
void update(ll si, ll ss, ll se, ll qs, ll qe, ll val)
{
    if (lazy[si] != 0)
    {
        ll dx = lazy[si];
        lazy[si] = 0;
        st[si] += dx * (se - ss + 1);
        // Pass the updates to children
        if (ss != se)
            lazy[2 * si] += dx, lazy[2 * si + 1] += dx;
    }

    if (ss > qe || se < qs)
        return;

    if (ss >= qs && se <= qe)
    {
        ll dx = (se - ss + 1) * val;
        st[si] += dx;

        // Pass updates to children
        if (ss != se)
            lazy[2 * si] += val, lazy[2 * si + 1] += val;
        return;
    }

    ll mid = (ss + se) / 2;
    update(2 * si, ss, mid, qs, qe, val);
    update(2 * si + 1, mid + 1, se, qs, qe, val);
    st[si] = st[2 * si] + st[2 * si + 1];
}

int main()
{
    // Update this
    ll n, q;
    cin >> n >> q;
    for (ll o = 1; o <= n; o++)
        cin >> li[o];
    build(1, 1, n);
    while (q--)
    {
        ll type, a, b, u, k;
        cin >> type;
        if (type == 1)
        {
            cin >> a >> b >> u;
            update(1, 1, n, a, b, u);
        }
        else
        {
            cin >> k;
            cout << query(1, 1, n, k, k) << '\n';
            // cout << st[]
        }
    }
    return 0;
}