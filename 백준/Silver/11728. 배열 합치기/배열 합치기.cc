#include <bits/stdc++.h>
using namespace std;

int A[1000001];
int B[1000001];

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n,m;
    cin >> n >> m;
    for(int i=0; i<n; i++)
        cin >> A[i];
    for(int i=0; i<m; i++)
        cin >> B[i];
    
    int a=0, b=0;
    for(int i=0; i<n+m; i++) {
        if((A[a]<B[b] && a!=n) || b==m) cout << A[a++] << ' ';
        else cout << B[b++] << ' ';
    }
}