#include <bits/stdc++.h>
using namespace std;

int D[1000001];

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    D[1]=0; //초기값 설정
    for(int k=2; k<=n; k++) {
        D[k] = D[k-1] +1;
        if(k%3==0) D[k] = min(D[k],D[k/3]+1);
        if(k%2==0) D[k] = min(D[k],D[k/2]+1);
    }
    cout << D[n];
}
