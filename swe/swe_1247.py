# 1247. [S/W 문제해결 응용] 3일차 - 최적 경로

# 회사에서 출발해서 모든 고객을 방문하고 집에 돌아오는 경로 중 가장 짧은 것을 찾아라
import sys
sys.stdin = open("swe_1247.txt", "r")

def cal_d(loc_1, loc_2):
    distance = abs(loc_1[0] - loc_2[0]) + abs(loc_1[1] - loc_2[1])
    return distance


def TSP(N, cur_dep=0, move_d=0):
    global min_d
    if cur_dep > N:
        if move_d < min_d:
            min_d = move_d
    pass

for t in range(1, int(input()) + 1):
    N = int(input()) # 고객의 수
    temp = tuple(map(int, input().split())) # 회사(0, 1) 집(2, 3) / 나머지 고객(N 개만큼)
    comp, home = (temp[0], temp[1]), (temp[2], temp[3])
    customers = [ (temp[i], temp[i + 1]) for i in range(4, (N + 2) << 1, 2) ]
    min_d = 0xffffff
    # 순서대로 1번 돌려서 거리 측정 -> 기준값으로 잡음


    # 재귀 호출하며 순회하는 함수 호출

    # print("#{} {}".format(t, min_d))