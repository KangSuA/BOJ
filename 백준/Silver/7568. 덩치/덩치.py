import sys
input = sys.stdin.readline

N = int(input())
student = []
for i in range(N):
  x, y = map(int,input().split())
  student.append((x,y,i))
  
student.sort(key = lambda x:(-x[0],-x[1]))

for i in range(N):
  rank = 1
  for j in range(0,i):
    if student[j][0] > student[i][0] and student[j][1] > student[i][1]:
      rank += 1
  student[i] += (rank,)

student.sort(key = lambda x:x[2])

for s in student:
  print(s[3],end=" ")