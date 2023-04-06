#include <bits/stdc++.h>
using namespace std;
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int n[3];
  cin >> n[0] >> n[1] >> n[2];
  sort(n,n+3);
  if(n[0]==n[2]) cout<<10000+n[0]*1000;
  else if((n[0]==n[1])||(n[1]==n[2])) cout<<1000+n[1]*100;
  else cout<<n[2]*100;
}