N = int(input())
for i in range(1,N+1):
    newN = list(str(i))
    newN = list(map(int,newN))
    cnt = 0
    for n in newN:
        if n%3==0 and n!=0:
            cnt += 1
    if not cnt:
        print(i,end="")
    else:
        for c in range(cnt):
            print("-",end="")
    print("",end=" ")