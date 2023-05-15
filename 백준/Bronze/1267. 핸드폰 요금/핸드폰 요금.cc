#include <bits/stdc++.h>
using namespace std;
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n,m=0,y=0;
  int t[20];
  cin >> n;
  for(int i=0; i<n; i++) {
    cin >> t[i];
    y+=((t[i]/30)+1)*10;
    m+=((t[i]/60)+1)*15;
  }
  if(m==y) cout << "Y M " << m;
  else if(m<y) cout << "M " << m;
  else cout << "Y " << y;
}