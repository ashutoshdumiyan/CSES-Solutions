#include <bits/stdc++.h>
using namespace std;

int li[200001], st[800001];

void build(int si, int ss, int se)
{
    if (ss == se)
    {
        st[si] = li[ss];
        return;
    }
    int mid = (ss + se) / 2;
    build(2 * si, ss, mid);
    build(2 * si + 1, mid + 1, se);
    st[si] = min(st[2 * si], st[2 * si + 1]);
}

int query(int si, int ss, int se, int qs, int qe)
{
    if (ss > qe || se < qs)
    {
        return INT_MAX;
    }
    if (ss >= qs && se <= qe)
    {
        return st[si];
    }
    int mid = (ss + se) / 2;
    int l = query(2 * si, ss, mid, qs, qe);
    int r = query(2 * si + 1, mid + 1, se, qs, qe);
    return min(l, r);
}

// Point update (to update one element)
void update(int si, int ss, int se, int qi)
{
    if (ss == se)
    {
        st[si] = li[qi];
        return;
    }
    int mid = (ss + se) / 2;
    if (qi <= mid)
    {
        update(2 * si, ss, mid, qi);
    }
    else
    {
        update(2 * si + 1, mid + 1, se, qi);
    }
    st[si] = min(st[2 * si], st[2 * si + 1]);
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
        int type, a, b;
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