#include <bits/stdc++.h>
using namespace std;

int r[1001];
int g[1001];
int b[1001];
int cost[1001][4];

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    for(int i=1; i<=n; i++)
        cin >> r[i] >> g[i] >> b[i];
    /*Initialize*/
    cost[1][0] = r[1];
    cost[1][1] = g[1];
    cost[1][2] = b[1];
    for(int i=2; i<=n; i++) {
        cost[i][0] = min(cost[i-1][1],cost[i-1][2]) + r[i];
        cost[i][1] = min(cost[i-1][0],cost[i-1][2]) + g[i];
        cost[i][2] = min(cost[i-1][0],cost[i-1][1]) + b[i];
    }
    cout << *min_element(cost[n],cost[n]+3);   
}