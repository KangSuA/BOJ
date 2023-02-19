#include <bits/stdc++.h>
using namespace std;
int g[7],b[7];
int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,k,y,room=0;
    bool s;
    cin >> n >> k;
    while(n--) {
        cin >> s >> y;
        if(s) b[y]++; //boy
        else g[y]++; //girl
    }
    for(int i=1;i<7;i++) {
        room += b[i]/k + g[i]/k;
        if(b[i]%k!=0) room++;
        if(g[i]%k!=0) room++;
    }
    cout << room;
}