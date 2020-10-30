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
    st[si] = st[2 * si] + st[2 * si + 1];
}

ll query(ll si, ll ss, ll se, ll qs, ll qe)
{
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

// Point update (to update one element)
void update(ll si, ll ss, ll se, ll qi)
{
    if (ss == se)
    {
        // return when you reach the node
        st[si] = li[qi];
        return;
    }
    ll mid = (ss + se) / 2;
    if (qi <= mid)
    {
        update(2 * si, ss, mid, qi);
    }
    else
    {
        update(2 * si + 1, mid + 1, se, qi);
    }
    st[si] = st[2 * si] + st[2 * si + 1];
}

int main()
{
    ll n, q;
    cin >> n >> q;
    for (ll o = 1; o <= n; o++)
        cin >> li[o];
    build(1, 1, n);
    while (q--)
    {
        ll type, a, b;
        cin >> type >> a >> b;
        if (type == 1)
        {
            li[a] = b;
            update(1, 1, n, a);
        }
        else
        {
            cout << query(1, 1, n, a, b) << '\n';
        }
    }
    return 0;
}