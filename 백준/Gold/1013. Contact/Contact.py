import sys
input = sys.stdin.readline

def yorn(wave):
  pattern = []
  flag = "NO"
  prev = ""
  for i in wave:
    if not pattern:
      pattern.append(i)
      flag="NO"
    elif pattern[0]=='0':
      if i=='1':
        flag="YES"
        prev = "0"
        pattern = []
      else:
        break
    elif pattern[0]=='1' and i=='1':
      pattern.append(i)
      if len(pattern)==3 and pattern[1]=='0' and prev=="1":
        pattern=[]
        flag="YES"
        prev="0"
        continue
      if len(pattern)<4:
        break
      else:
        flag = "YES"
    elif pattern[0]=='1' and i=='0':
      if len(pattern)>3 and pattern[-1]=='1':
        if pattern[-2]=='1':
          pattern = ['1']
          prev = "1"
        else:
          pattern = []
        flag="NO"
      pattern.append(i)
  return flag

T = int(input())
for i in range(T):
  wave = list(input().rstrip())
  print(yorn(wave))