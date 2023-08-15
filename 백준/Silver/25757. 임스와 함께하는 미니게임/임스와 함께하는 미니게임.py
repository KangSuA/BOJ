N, G = input().split()
player = [input().rstrip() for _ in range(int(N))]
sp = set(player)
dic = {'Y':1,'F':2,'O':3}
print(len(sp)//dic[G])