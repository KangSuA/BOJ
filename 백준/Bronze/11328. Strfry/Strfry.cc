#include <bits/stdc++.h>
using namespace std;
int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    while(n--) {
        string a,b;
        int i;
        char cha[26]={}, chb[26]={};
        cin >> a >> b;
        for(char e : a) cha[e-'a']++;
        for(char e : b) chb[e-'a']++;
        for(i=0;i<26;i++) {
            if(cha[i]!=chb[i]) {
                cout<< "Impossible\n";
                break;
            }
        }
        if(i==26) cout<< "Possible\n";
    }
}