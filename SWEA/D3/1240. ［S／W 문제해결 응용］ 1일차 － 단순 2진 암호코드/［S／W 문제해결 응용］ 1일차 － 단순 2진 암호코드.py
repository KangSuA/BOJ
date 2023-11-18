T = int(input())
rule = ["0001101","0011001","0010011","0111101","0100011","0110001","0101111","0111011","0110111","0001011"]
rules = dict(zip(rule,range(10)))
for t in range(1,T+1):
    N,M = map(int,input().split())
    line = []
    for i in range(N):
        lines = list(input())
        if "1" in lines:
            line = lines
    for idx in range(len(line)-1,0,-1):
        if line[idx]=="1":
            break
    code = line[idx-55:idx+1]
    res = []
    for i in range(0,56,7):
        res.append(int(rules["".join(code[i:i+7])]))
    cal = (sum(res[::2])*3 + sum(res[1::2]))%10
    print(f'#{t} {sum(res)}' if cal%10==0 else f'#{t} 0')