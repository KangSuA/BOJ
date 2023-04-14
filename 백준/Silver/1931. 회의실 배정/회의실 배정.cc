#include <bits/stdc++.h>
using namespace std;
pair<int,int> s[100002]; //end -> start 순으로 저장
int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    for(int i=0; i<n; i++)
        cin >> s[i].second >> s[i].first;
    sort(s,s+n);
    int cnt=0, e=0;
    for(int i=0; i<n; i++) {
        if(e > s[i].second) continue;
        cnt++;
        e = s[i].first;
    }
    cout << cnt;
}