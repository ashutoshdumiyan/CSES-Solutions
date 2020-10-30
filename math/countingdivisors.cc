#include <bits/stdc++.h>
using namespace std;

int divisors(int num)
{
    int i = 1;
    int res = 0;

    while (i * i <= num)
    {
        if (num % i == 0)
        {
            if (num / i == i)
            {
                res += 1;
            }
            else
            {
                res += 2;
            }
        }
        i += 1;
    }
    return res;
}

int main()
{
    int n;
    cin >> n;
    while (n--)
    {
        int num;
        cin >> num;
        cout << divisors(num) << '\n';
    }
    return 0;
}