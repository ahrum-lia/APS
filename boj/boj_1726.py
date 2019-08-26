import sys
sys.stdin = open("./boj_1726.txt", "r")

# 로봇의 이동을 제어하는 명령어: Go k(현재 향하고 있는 방향으로 k칸만큼 움직임)
#                           : Turn dir(왼 또는 오 이며 90도 회전)

# 0은 갈 수 있음, 1은 못 감
# 로봇을 원하는 위치, 원하는 방향으로 바라보게 하는데 최소 몇 번의 명령이 필요한지 구해라

# move function -> 재귀
def move(cur_r, cur_c, cur_dir, comm_cnt=0, k=0):
    global e_r, e_c, e_dir, min_command
    
    # 종료 조건 1: 목표지점에 도달헀다. => 최소 명령 횟수와 비교하고 명령 횟수를 갱신해준다
    if cur_r == e_r and cur_c == e_c and cur_dir == e_dir:
        if comm_cnt < min_command:
            min_command = comm_cnt
        return

    # 종료 조건 2: 현재 명령한 횟수가 최소 명령 횟수보다 크다 => 그냥 return 
    if comm_cnt >= min_command:
        return


    # 재귀 호출 경우의 수: 회전(2방- 왼, 오로 90도) * k칸 이동
    # k만큼 이동하는 것 적용해줘야함
    for n_dir in turn[cur_dir]:
        n_r, n_c = cur_r + delta[n_dir][0], cur_c + delta[n_dir][1]
        if 0 <= n_r < M and 0 <= n_c < N and board[n_r][n_c] == 0:
            # k칸 이동 재귀 호출
            for i in range(1, )
            pass


# 동: 1 / 서: 2 / 남: 3 / 북: 4
delta = {1: (0, 1), 2:(0, -1), 3:(1, 0), 4:(-1, 0)}

# turn
turn = {1: [3, 4], 2:[3, 4], 3:[1, 2], 4:[1, 2]}

M, N = map(int, input().split()) # 가로, 세로 (<=100)
board = []
for _ in range(M):
    board.append(list(map(int, input().split())))

s_r, s_c, s_dir = map(int, input().split())
e_r, e_c, e_dir = map(int, input().split())

min_command = 100000000000
move(s_r, s_c, s_dir)
print(min_command)
