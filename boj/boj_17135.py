# boj 캐슬디펜스
import sys
sys.stdin = open("boj_17135.txt", "r")

for t in range(1, int(input()) + 1):
    R, C, D = map(int, input().split())
    board = [ list(map(int, input().split())) for _ in range(R) ]
    max_death = 0
    castles = [ (R, _) for _ in range(C) ]
    # print(castles)

    enems_i = []
    for r in range(R):
        for c in range(C):
            if board[r][c] == 1:
                enems_i.append((r, c))
    enems_cnt = len(enems_i)

    # 궁수 좌표값의 조합을 생성
    for i in range(1 << C):
        comb_cnt = 0
        idxs = [0] * C
        for j in range(R):
            if i & (1 << j) != 0:
                comb_cnt += 1
                idxs[j] = 1
        if comb_cnt != 3:
            continue

        death = 0
        while enems_cnt > 0:
            # 궁수의 좌표값을 돌면서 가장 가깝고 & 왼쪽에 있고 & 사정거리 안에 있는 적을 제거

            # death 수 측정

            # max_death 갱신
            pass