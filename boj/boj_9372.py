import sys
sys.stdin = open("boj_9372.txt", "r")

from collections import deque
# DEQUE
# appendleft(), pop(), append(), popleft()




# N개국 여행
# 최대한 적은 종류의 비행기를 타고 국가들을 이동
# 중간에 다른 국가를 거쳐가도(방문했던 나라라도) 가능

# BFS 함수 만들기
# 한 정점을 처음에 선택해서 경로 탐색
# 다음 경로부터 가지치기
def shortest():
    pass

# 테스트 케이스의 수 T (T <= 100)
for tc in range(int(input())):
    N, M = map(int, input().split()) # N :국가의 수 (2 <= N <= 1000), M : 비행기의 종류 (1 <= M <= 10000)
    G = [[] for _ in range(N + 1)]

    for _ in range(M):
        depart, arrive = map(int, input().split())
        G[depart].append(arrive)
        G[arrive].append(depart)

