#include <bits/stdc++.h>
using namespace std;
int a[11];
int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,k;
    cin >> n >> k;
    for(int i=0; i<n; i++) {
        cin >> a[i];
    }
    int cnt = 0, r = k;
    for(int i=n-1; i>=0; i--) {
        if(r<a[i]) continue;
        cnt += r/a[i];
        r = k%a[i];
        if(r==0) break;
    }
    cout << cnt;
}