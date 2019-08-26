import sys
sys.stdin = open("boj_17143.txt", "r")

# 낚시왕 초기 위치 = (-1, -1) // (R -1, C -1) 에 도착하면 이동을 멈춘다.
# 1. 낚시왕이 오른쪽으로 한 칸 이동
# 2. 낚시왕이 있는 열에서 가장 가까운 상어를 잡는다. 상어를 잡으면 상어는 사라진다
# 3. 상어 이동 (경계에 도착하면 방향을 반대로 바꾼다)
# 4. 상어가 한 칸에 2마리 이상 있는 경우는 크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹는다


def move_fishes(R, C, old_board):
    new_board = [[ [] for _ in range(C) ] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if board[r][c]:
                for sha_info in board[r][c]:
                    c_r, c_c, c_speed, c_dir, c_size = r, c, sha_info['speed'], sha_info['direction'], sha_info['size']
                    n_r, n_c = c_r + (dirs[c_dir][0] * c_speed), c_c + (dirs[c_dir][1] * c_speed)

                    if 0 <= n_r < R and 0 <= n_c < C:
                        new_board[n_r][n_c].append({'speed': c_speed, 'direction': c_dir, 'size': c_size})
                    else:
                        # 크기 초과가 나지 않을때까지 숫자와 방향을 바꿔줘야함
                        if c_dir == 1:
                            n_dir = 2
                            n_r =  c_speed - c_r
                        elif c_dir == 2:
                            n_dir = 1
                            n_r = c_speed - (R - 1 - c_r)
                        elif c_dir == 3:
                            n_dir = 4
                            n_c = c_speed - (C - 1 - c_c)
                        else:
                            n_dir = 3
                            n_c = c_speed - c_c
                        new_board[n_r][n_c].append({'speed': c_speed, 'direction': n_dir, 'size': c_size})
                
        return new_board


def muk_e_sasle(R, C, new_board):
    biggest_shark_size = -1
    biggest_shark_info = -1
    for r in range(R):
        for c in range(C):
            if len(new_board[r][c]) > 1:
                for i in range(len(board[r][c])):
                    if new_board[r][c][i]['size'] > biggest_shark_size:
                        biggest_shark_size = new_board[r][c][i]['size']
                        biggest_shark_info = new_board[r][c][i]

                board[r][c] = [biggest_shark_info]

    return new_board



# 출력: 낚시왕이 잡은 상어 크기의 합
for t in range(1, int(input()) + 1):
    R, C, M = map(int, input().split())
    if M == 0:
        print(0)
        continue
    sharks_infos = [list(map(int, input().split())) for _ in range(M)] # r, c, 속력, 이동방향, 크기 (좌표가 1부터 시작)
    board = [[ [] for _ in range(C) ] for _ in range(R)]
    caught_fishes = 0
    dirs = [(), (-1, 0), (1, 0), (0, 1), (0, -1)] # 1:위, 2: 아래, 3:오른, 4:왼

    for sha_info in sharks_infos:
        r, c, = sha_info[0], sha_info[1]
        board[r-1][c-1].append({'speed': sha_info[2], 'direction': sha_info[3], 'size': sha_info[4]})
    
    for naksi_king_c in range(C):
        # naksi_king_c에 있는 물고기중 r값이 제일 작은 것 제거(pop ?) & 먹은 물고기 숫자 올리기
        for i in range(R):
            if board[i][naksi_king_c]:
                caught_info = board[i][naksi_king_c].pop()
                caught_fishes += caught_info['size']
        # 물고기 이동(함수 만들기)
        new_board = move_fishes(R, C, board)
        # 물고기 제거
        muk_e_sasle(R, C, new_board)
    print(caught_fishes)



