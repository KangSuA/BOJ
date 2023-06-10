#include <bits/stdc++.h>
using namespace std;
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int a,b,c;
  cin >> a >> b >> c;
  int d,e,f;
  d = min({a,b,c}); //algorithm헤더
  f = max({a,b,c}); //{}을 사용 2개 이상 가능
  e = a+b+c-d-f;
  cout << d <<' '<<e<<' '<<f;
}