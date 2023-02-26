#include <bits/stdc++.h>
using namespace std;

int num[100001];
int d[100001];

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, m;
    cin >> n >> m;
    for(int i=1; i<=n; i++)
        cin >> num[i];
    d[0] = 0;
    d[1] = num[1];
    for(int i=2; i<=n; i++)
        d[i] = d[i-1] + num[i];
    while(m--) {
        int a,b;
        cin >> a >> b;
        cout << d[b] - d[a-1] <<'\n';
    }
}