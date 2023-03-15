N = int(input())
sand = [list(map(int,input().split())) for _ in range(N)]
r,c = N//2, N//2

#방향 별 이동 횟수 [1,1,2,2,3...]
t_rotation_cnt = [i//2+1 for i in range(N*2-1)] 
t_direction = [(0,-1),(1,0),(0,1),(-1,0)] #좌하우상
#이동 방향에 따른 모래 이동 비율/중심기준(행,열,비율)
move_direction = [[(-1, 1, 0.01), (1, 1, 0.01), (-2, 0, 0.02), (2, 0, 0.02), (-1, 0, 0.07), (1, 0, 0.07), (-1, -1, 0.1), (1, -1, 0.1), (0, -2, 0.05), (0, -1, 0.55)], [(-1, -1, 0.01), (-1, 1, 0.01), (0, -2, 0.02), (0, 2, 0.02), (0, -1, 0.07), (0, 1, 0.07), (1, -1, 0.1), (1, 1, 0.1), (2, 0, 0.05), (1, 0, 0.55)],
 [(-1, -1, 0.01), (1, -1, 0.01), (-2, 0, 0.02), (2, 0, 0.02), (-1, 0, 0.07), (1, 0, 0.07), (-1, 1, 0.1), (1, 1, 0.1), (0, 2, 0.05), (0, 1, 0.55)], [(1, -1, 0.01), (1, 1, 0.01), (0, -2, 0.02), (0, 2, 0.02), (0, -1, 0.07), (0, 1, 0.07), (-1, -1, 0.1), (-1, 1, 0.1), (-2, 0, 0.05), (-1, 0, 0.55)]]

# , 현재 이동 횟수, 현재 이동 방향 idx
rotation_time, move_time, direction = 0,0,0
res = 0
while (r,c) != (0,0):
  if move_time == t_rotation_cnt[rotation_time]:
    move_time = 0
    direction += 1
    direction %= 4
    rotation_time += 1
  r+=t_direction[direction][0]
  c+=t_direction[direction][1]

  y=sand[r][c] #이동한 모래 양

  tot = 0
  for dx, dy, percentage in move_direction[direction]:
    if percentage == 0.55:
      move_sand = y-tot #move_sand는 해당 칸으로 이동하는 모래 양
    else:
      move_sand = int(y*percentage)
    nr, nc = r+dx, c+dy
    tot += move_sand

    if 0<=nr<N and 0<=nc<N: #격자 범위 내인지 확인
      sand[nr][nc] += move_sand
    else: #소실된 모래 양
      res += move_sand

  move_time += 1
print(res)