#include <bits/stdc++.h>
using namespace std;
int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n,p,i=1;
    bool no=0;
    stack<int> s;
    queue<char> ch;
    cin >> n;
    while(n--) {
        cin >> p;
        if(i<=p) {
            while(i!=p+1) {
                 s.push(i++);
                 ch.push('+');
            }
            s.pop();
            ch.push('-');
        }
        else {
            if(s.top()==p) {
                s.pop();
                ch.push('-');
            }
            else no=1;
        }
    }
    if(no) cout << "NO\n";
    else {
        while(!ch.empty()) {
            cout<< ch.front() <<"\n";
            ch.pop();
        }
    }
}