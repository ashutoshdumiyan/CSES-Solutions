#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;

ll split(ll li[], ll mid, ll n) {
    ll pieces = 1;
    ll tempSum = 0;
    for (ll i = 0; i < n; i++) {
        if (tempSum + li[i] > mid) {
            pieces += 1;
            tempSum = li[i];
        }
        else {
            tempSum += li[i];
        }
    }
    return pieces;
}

int main() {
    ll n, k, mx, s;
    cin >> n >> k;
    ll li[n];
    mx = 0;
    s = 0;
    for (ll i = 0; i < n; i++) {
        cin >> li[i];
        s += li[i];
        if (li[i] > mx)
            mx = li[i];
    }
    ll lo = mx;
    ll hi = s;

    while (lo < hi){
        ll mid = (lo + hi) / 2;
        ll pieces = split(li, mid, n);
        if (pieces > k) {
            lo = mid + 1;
        }
        else {
            hi = mid;
        }
    }
    cout << lo;

    return 0;
}