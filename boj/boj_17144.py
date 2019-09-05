# boj 미세먼지 안녕!
import sys
sys.stdin = open("boj_17144.txt", "r")
#
# # 확산 함수
# def spread(arr):
#     while arr:
#         x, y, dust = arr.pop(0)
#         sp_amount = dust // 5
#         if sp_amount < 1:
#             continue
#         total_sp = 0
#         for d in range(4):
#             nx, ny = x + delta[d][0], y + delta[d][1]
#             if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != -1:
#                 board[nx][ny] += sp_amount
#                 total_sp += sp_amount
#         board[x][y] -= total_sp
#
# def clean():
#     c1, c2 = cleaners[0], cleaners[1]
#     pre1= (c1[0] -1, c1[1])
#     board[pre1[0]][pre1[1]] = 0
#
#     pre2 = (c2[0] + 1, c2[1])
#     board[pre2[0]][pre2[1]] = 0
#
#     while pre1 != c1:
#         if pre1[1] == 0 and pre1[0] != 0:
#             cx, cy = pre1[0], pre1[1]
#             pre1 = (cx -1, cy)
#             board[cx][cy] = board[pre1[0]][pre1[1]]
#
#         elif pre1[0] == 0 and pre1[1] != (C -1):
#             cx, cy = pre1[0], pre1[1]
#             pre1 = (cx, cy+1)
#             board[cx][cy] = board[pre1[0]][pre1[1]]
#
#         elif pre1[1] == (C - 1) and pre1[0] != c1[0]:
#             cx, cy = pre1[0], pre1[1]
#             pre1 = (cx + 1, cy)
#             board[cx][cy] = board[pre1[0]][pre1[1]]
#
#         elif pre1[0] == c1[0]:
#             cx, cy = pre1[0], pre1[1]
#             pre1 = (cx, cy -1)
#             board[cx][cy] = board[pre1[0]][pre1[1]]
#
#     while pre2 != c2:
#         if pre2[1] == 0 and pre2[0] < (R -1):
#             cx, cy = pre2[0], pre2[1]
#             pre2 = (cx + 1, cy)
#             board[cx][cy] = board[pre2[0]][pre2[1]]
#
#         elif pre2[0] == (R -1) and pre2[1] < (C -1):
#             cx, cy = pre2[0], pre2[1]
#             pre2 = (cx, cy+1)
#             board[cx][cy] = board[pre2[0]][pre2[1]]
#
#         elif pre2[1] == (C - 1) and pre2[0] != c2[0]:
#             cx, cy = pre2[0], pre2[1]
#             pre2 = (cx -1, cy)
#             board[cx][cy] = board[pre2[0]][pre2[1]]
#
#         elif pre2[0] == c2[0]:
#             cx, cy = pre2[0], pre2[1]
#             pre2 = (cx, cy-1)
#             board[cx][cy] = board[pre2[0]][pre2[1]]
#
#
# for test_case in range(1, int(input()) + 1):
#     R, C, T = map(int, input().split()) # 행, 열, T초 지난 후 미세먼지 양 출력
#
#     board = [ list(map(int, input().split())) for _ in range(R) ]
#
#     delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#     cleaners = [] # 0번이 위에 클리너, 1번이 아래 클리너
#     dusts = []
#     t = 0
#     for __ in range(R):
#         for ___ in range(C):
#             if board[__][___] == -1:
#                 cleaners.append((__, ___))
#         if len(cleaners) == 2:
#             break
#     while t < T:
#         # -1: 공기청정기의 위치, 0보다 크면 미세먼지가 있는 곳
#         # 초기화: 공기청정기의 위치 찾기, 처음 미세먼지의 위치 찾기
#         dusts = []
#         for r in range(R):
#             for c in range(C):
#                 if board[r][c] > 0:
#                     dusts.append((r, c, board[r][c]))
#         # 확산
#         spread(dusts)
#
#         # 제거
#         clean()
#         t += 1
#
#     res = 0
#     for i in range(R):
#         for j in range(C):
#             if board[i][j] > 0:
#                 res += board[i][j]
#
#     print("#{} {}".format(test_case, res))
#



def spread(arr):
    while arr:
        x, y, dust = arr.pop(0)
        sp_amount = dust // 5
        if sp_amount < 1:
            continue
        total_sp = 0
        for d in range(4):
            nx, ny = x + delta[d][0], y + delta[d][1]
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != -1:
                board[nx][ny] += sp_amount
                total_sp += sp_amount
        board[x][y] -= total_sp

def clean():
    c1, c2 = cleaners[0], cleaners[1]
    pre1= (c1[0] -1, c1[1])
    board[pre1[0]][pre1[1]] = 0

    pre2 = (c2[0] + 1, c2[1])
    board[pre2[0]][pre2[1]] = 0

    while pre1 != c1:
        if pre1[1] == 0 and pre1[0] != 0:
            cx, cy = pre1[0], pre1[1]
            pre1 = (cx -1, cy)
            board[cx][cy] = board[pre1[0]][pre1[1]]

        elif pre1[0] == 0 and pre1[1] != (C -1):
            cx, cy = pre1[0], pre1[1]
            pre1 = (cx, cy+1)
            board[cx][cy] = board[pre1[0]][pre1[1]]

        elif pre1[1] == (C - 1) and pre1[0] != c1[0]:
            cx, cy = pre1[0], pre1[1]
            pre1 = (cx + 1, cy)
            board[cx][cy] = board[pre1[0]][pre1[1]]

        elif pre1[0] == c1[0]:
            cx, cy = pre1[0], pre1[1]
            pre1 = (cx, cy -1)
            board[cx][cy] = board[pre1[0]][pre1[1]]
    board[c1[0]][c1[1] +1] =0
    while pre2 != c2:
        if pre2[1] == 0 and pre2[0] < (R -1):
            cx, cy = pre2[0], pre2[1]
            pre2 = (cx + 1, cy)
            board[cx][cy] = board[pre2[0]][pre2[1]]

        elif pre2[0] == (R -1) and pre2[1] < (C -1):
            cx, cy = pre2[0], pre2[1]
            pre2 = (cx, cy+1)
            board[cx][cy] = board[pre2[0]][pre2[1]]

        elif pre2[1] == (C - 1) and pre2[0] != c2[0]:
            cx, cy = pre2[0], pre2[1]
            pre2 = (cx -1, cy)
            board[cx][cy] = board[pre2[0]][pre2[1]]

        elif pre2[0] == c2[0]:
            cx, cy = pre2[0], pre2[1]
            pre2 = (cx, cy-1)
            board[cx][cy] = board[pre2[0]][pre2[1]]
    board[c2[0]][c2[1] + 1] = 0

R, C, T = map(int, input().split()) # 행, 열, T초 지난 후 미세먼지 양 출력

board = [ list(map(int, input().split())) for _ in range(R) ]

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
cleaners = [] # 0번이 위에 클리너, 1번이 아래 클리너
dusts = []
t = 0
for __ in range(R):
    for ___ in range(C):
        if board[__][___] == -1:
            cleaners.append((__, ___))
    if len(cleaners) == 2:
        break
while t < T:
    # -1: 공기청정기의 위치, 0보다 크면 미세먼지가 있는 곳
    # 초기화: 공기청정기의 위치 찾기, 처음 미세먼지의 위치 찾기
    dusts = []
    for r in range(R):
        for c in range(C):
            if board[r][c] > 0:
                dusts.append((r, c, board[r][c]))
    # 확산
    spread(dusts)

    # 제거
    clean()
    t += 1

res = 0
for i in range(R):
    for j in range(C):
        if board[i][j] > 0:
            res += board[i][j]

print(res)