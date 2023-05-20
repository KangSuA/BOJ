#include <bits/stdc++.h>
using namespace std;
int digit[10];
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n,res=0;
  cin >> n;
  while(n>0) {
    digit[n%10]++;
    n/=10;
  }
  for(int i=0;i<10;i++) {
    if(i==6 || i==9) continue;
    res=max(res,digit[i]);
  }
  res=max(res,(digit[6]+digit[9]+1)/2);
  cout << res;
}