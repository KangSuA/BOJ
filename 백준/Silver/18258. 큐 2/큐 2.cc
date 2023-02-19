#include <bits/stdc++.h>
using namespace std;
int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    queue<int> Q;
    int n,x=0;
    string s;
    cin >> n;
    while(n--) {
        cin >> s;
        if(s=="push") {
            cin >> x;
            Q.push(x);
        }
        else if(s=="pop") {
            if(Q.empty()) cout << -1 << "\n";
            else {
                cout << Q.front() << "\n";
                Q.pop();
            }
        }
        else if(s=="size") cout << Q.size() << "\n";
        else if(s=="empty") cout << Q.empty() << "\n";
        else if(s=="front") {
            if(Q.empty()) cout << -1 << "\n";
            else cout << Q.front() << "\n";
        }
        else {
            if(Q.empty()) cout << -1 << "\n";
            else cout << Q.back() << "\n";
        }
    }
}