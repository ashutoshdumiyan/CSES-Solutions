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
    if (qs > se || qe < ss)
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