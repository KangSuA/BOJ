T = int(input())
for t in range(1,T+1):
    n = input()
    cnt = 0
    for i in range(len(n)-1):
        if n[i]!=n[i+1]:
            cnt += 1
    if n[0]=='1':
        cnt += 1
    print(f'#{t} {cnt}')