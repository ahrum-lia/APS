import sys
sys.stdin = open("swe_2383.txt", "r")

# locs_and_dist 배열에 들어있는 정보를 꺼내서 쓴다
# 사람의 총 명수, 현재 사람의 번호, 계단의 번호
# 새로 생성할 데이터: 1번계단, 2번계단에 몇 명있는지
# stair1, stair2 에는 배열을 넘기는데 사람들을 append 해준다
def recur(M, cur_P, cur_S, cur_T, stair1, stair2):
    global min_time
    # 종료 조건
    if cur_P == (M - 1):
        # 최소 시간이면 최소 시간 갱신(전역으로)
        if cur_T < min_time:
            min_time = cur_T
            return

    # 넘어온 사람 정보를 가지고 시간을 계산 (계단의 사람 제한 조건 처리)
    # cur_T를 갱신


    # 최소 시간보다 길면 종료

    # 재귀 호출
    for cur_P in range(M):
        recur(M, cur_P, 0, cur_T)
        recur(M, cur_P, 1, cur_T)



for t in range(1, int(input()) + 1):
    N = int(input())
    board = [ list(map(int, input().split())) for _ in range(N)]
    locs_and_dist = [] # [pc, pr, (distance from stair1, depth of stair1), (distance from stair2, depth of stair2)]
    stairs = []
    min_time = 10000000

    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:

                continue
            elif board[i][j] == 1:
                locs_and_dist.append([i, j])
            else:
                stairs.append((i, j, board[i][j]))

    M = len(locs_and_dist) # number of people

    for i in range(M):
        D1 = abs(locs_and_dist[i][0] - stairs[0][0]) + abs(locs_and_dist[i][1] - stairs[0][1])
        D2 = abs(locs_and_dist[i][0] - stairs[1][0]) + abs(locs_and_dist[i][1] - stairs[1][1])
        locs_and_dist[i] += [(D1, stairs[0][2]), (D2, stairs[1][2])]

    print(f'#{t} {locs_and_dist}')