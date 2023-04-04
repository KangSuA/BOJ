#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
stack<pair<int,int>> tower;
int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,h;
    cin >> n;
    tower.push({100000001,0});
    for(int i=1; i<= n; i++) {
        cin >> h;
        while(tower.top().X < h) tower.pop();
        cout << tower.top().Y << " ";
        tower.push({h,i});
    }
}