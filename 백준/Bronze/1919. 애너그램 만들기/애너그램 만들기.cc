#include <bits/stdc++.h>
using namespace std;
int comp[26];
int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    string a,b;
    int res=0;
    cin >> a >> b;
    for(char c : a) comp[c-'a']++;
    for(char c : b) comp[c-'a']--;
    for(int i : comp) res += abs(i);
    cout << res;
}