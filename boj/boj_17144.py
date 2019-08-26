import sys
sys.stdin = open("boj_17144.txt", "r")

#   1초 동안 순서대로
# 미세먼지가 확산된다(미세먼지가 있는 칸에서 4방향으로)
# 확산되는 양은 1/5 이고, 소수점은 버린다
# 원래 칸에 남은 미세먼지 양은 (원래양) - (원래양의 1/5 * 확산된 방향의 갯수)

# 공기청정기 작동
# 위쪽 공기청정기는 반시계방향, 아래쪽은 시계방향으로
# 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다

# R, C, T

# 미세먼지 확산
def spreading(R, C):
    for r in range(R):
        for c in range(C):
            if board[r][c] > 0:
                dust_amount = board[r][c]
                spreaded = dust_amount // 5
                spreaded_cnt = 0
                if spreaded <= 0:
                    continue
                # 4방향으로 확산
                # 인접한 방향이 공기청정기이면 확산되지 않음
                # 확산된 후 원래 칸의 먼지의 양을 줄여줘야 함
                for i in range(4):
                    # 경계 체크, 공기청정기 체크
                    next_r, next_c = r + dirs[i][0], c + dirs[i][1]
                    if 0 <= next_r < R and 0 <= next_c < C and board[next_r][next_c] > -1:
                        board[next_r][next_c] += spreaded
                        spreaded_cnt += 1
                board[r][c] -= spreaded * spreaded_cnt
                
# 공기청정기 작동
def clean(head_i, bottom_i):
    # 1. head_i 반시계 방향으로 미세먼지 밈 (우(R까지) - 상(C0까지) - 좌(R0까지) - 하(C까지) - 청정기로 돌아오지 않았다면 돌아올때까지 우)
    nr, nc = head_i[0], head_i[1] + 1
    cur_val = board[head_i[0]][head_i[1]]
    next_val = board[nr][nc]
    while (nr, nc) == head_i:
        



    # 2. bottom_i 시계 방향으로 미세먼지 밈 (우 - 하 - 좌 - 상 -  우 )
    pass

for t in range(1, int(input()) + 1):
    R, C, T = map(int, input().split())
    board = [ list(map(int, input().split())) for _ in range(R)]
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cleaner_i = []

    for i in range(R):
        for j in range(C):
            if board[i][j] == -1:
                cleaner_i.append((i, j))

    for _ in range(T):
        # 미세먼지 확산
        spreading()
        # 공기 청정기 작동
        clean(cleaner_i[0], cleaner_i[1])

    # board 를 돌면서 미세먼지의 양 측정한뒤 print