T = 10
for t in range(1,T+1):
    input()
    matrix = []
    for i in range(100):
        matrix.append(list(map(int,input().split())))
    res = [0]*202
    for i in range(100):
        for j in range(100):
            if i==j:
                res[200] += matrix[i][j]
            elif i+j==99:
                res[201] += matrix[i][j]
            res[j] += matrix[i][j]
        res[i+100] += sum(matrix[i])
    print(f'#{t} {max(res)}')