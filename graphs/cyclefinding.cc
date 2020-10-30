#include <bits/stdc++.h>
using namespace std;
const int INF = 1000000000;

struct Edge
{
    int a, b, cost;
};

int main()
{
    int n, m;
    vector<Edge> edges;
    cin >> n >> m;
    for (int o = 0; o < m; o++)
    {
        int x, y, z;
        cin >> x >> y >> z;
        edges.push_back({x, y, z});
    }
    vector<int> d(n);
    vector<int> p(n, -1);
    int x;
    for (int i = 0; i < n; ++i)
    {
        x = -1;
        for (Edge e : edges)
        {
            if (d[e.a] + e.cost < d[e.b])
            {
                d[e.b] = d[e.a] + e.cost;
                p[e.b] = e.a;
                x = e.b;
            }
        }
    }

    if (x == -1)
    {
        cout << "NO";
    }
    else
    {
        for (int i = 0; i < n; ++i)
            x = p[x];

        vector<int> cycle;
        int v = x;
        while (true)
        {
            cout << "abc"
                 << " " << x << " " << v << '\n';
            cycle.push_back(v);
            if (v == x && cycle.size() > 1)
                break;
            v = p[v];
        }
        reverse(cycle.begin(), cycle.end());

        cout << "YES" << '\n';
        for (int v : cycle)
            cout << v << ' ';
        cout << endl;
    }
    return 0;
}