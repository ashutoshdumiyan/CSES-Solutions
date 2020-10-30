#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main() {
    int n, li[20];
    cin >> n;
    ll s = 0, res = 0;
    for(int u=0;u<n;u++){
        cin >> li[u];
        s += li[u];
    }
    for(int i = 0; i< 1<<n; i++) {
        ll temp = 0;
        for(int j=0;j<n;j++){
            if(i>>j&1) temp += li[j];
        }
        if(temp <= s/2) res = max(res, temp);
    }
    cout << s - 2 * res;
    return 0;
}