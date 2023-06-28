import sys
input = sys.stdin.readline

sdocu = [list(map(int, input().split())) for _ in range(9)]
check = True
zeros = [(i,j) for i in range(9) for j in range(9) if sdocu[i][j]==0]

def Garo(x, num):
    for i in range(9):
        if sdocu[x][i] == num:
            return False
    return True


def Sero(y, num):
    for i in range(9):
        if sdocu[i][y] == num:
            return False
    return True


def Square(x, y, num):
    for i in range(3):
        for j in range(3):
            if sdocu[3*(x // 3) + i][3*(y // 3) + j] == num:
                return False
    return True


def solve(depth):
    global check
    if depth == len(zeros):
        for i in range(9):
            print(*sdocu[i])
        check = False
        return

    for i in range(1, 10):
        x, y = zeros[depth]
        if Garo(x, i) and Sero(y, i) and Square(x, y, i) and check:
            sdocu[x][y] = i
            solve(depth+1)
            sdocu[x][y] = 0

solve(0)