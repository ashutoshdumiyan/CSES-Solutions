#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int li[n];
    int high = -1;
    for (int o = 0; o < n; o++)
    {
        cin >> li[o];
        high = max(high, li[o]);
    }
    int divisors[high + 1];
    for (int i = 0; i < n; i++)
    {
        int j = 1;
        while (j * j <= li[i])
        {
            if (li[i] % j == 0)
            {
                divisors[j] += 1;
                if (j != li[i] / j)
                    divisors[li[i] / j] += 1;
            }
            j += 1;
        }
    }
    for (int u = high; u >= 1; u--)
    {
        if (divisors[u] > 1)
        {
            cout << u << '\n';
            break;
        }
    }
    return 0;
}