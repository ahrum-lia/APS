# 점심 식사시간

import sys
sys.stdin = open("swe_2383.txt", "r")

#--------------------정답코드----------------------------------
for _ in range(1, int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for __ in range(N)]
    stair = []
    result = 0xffffff

    person = []
    for iy in range(N):
        for ix in range(N):
            if arr[iy][ix] == 1:
                temp = []
                for i in stair:
                    temp.append(abs(ix - i[0]) + abs(iy - i[1]) + 1 + i[2])
                else:
                    person.append(temp)

    for i in range(2 ** len(person) + 1):
        first = []
        secon = []

        for j in range(len(person)):
            if i & 1 << j:
                first.append(person[j][0])
            else:
                secon.append(person[j][1])
        first.sort()
        secon.sort()

        for i in range(len(first) -3):
            if first[i + 3] - first[i] < stair[0][2]:
                first[i + 3] = first[i] + stair[0][2]
            for j in range(len(secon) -3):
                if secon[j + 3] - secon[i] < stair[1][2]:
                    secon[j + 3] = secon[i] + stair[1][2]

            temp_result = max(max(first) if first else 0, max(secon) if secon else 0)
            result = min(temp_result, result)

    print("#{} {}".format(_, result))






#-----------------------여기서부터 내코드----------------------------------
# class Person:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.dis_1 = None
#         self.dis_2 = None
#
#     def set_dis(self, dis_1_loc, dis_2_loc):
#         self.dis_1 = abs(self.x - dis_1_loc[0]) + abs(self.y - dis_1_loc[1])
#         self.dis_2 = abs(self.x - dis_2_loc[0]) + abs(self.y - dis_2_loc[1])
#
# def move(queue, len_stair):
#     time = 0
#     down = [False] * len(queue)
#     down_cnt = 0
#     finish = 0
#
#     while finish < len(queue):
#         if down_cnt < 3:
#             for k in range(len(queue)):
#                 if down_cnt >= 3 and queue[k] < 0:
#                     break
#                 queue[k] -= 1
#                 if queue[k] < -len_stair:
#                     continue
#
#                 elif queue[k] <= 0 and down_cnt < 3 and down[k] == False:
#                     down_cnt += 1
#                     down[k] = True
#         else:
#             for d in range(finish, finish + 3):
#                 if queue[d] == -len_stair:
#                     down_cnt -= 1
#                     finish += 1
#                 queue[d] -= 1
#     return time
#
# for _ in range(1, int(input()) + 1):
#     min_time = 0xffff
#     N = int(input())
#     board = [list(map(int, input().split())) for _ in range(N)]
#
#     people = [] # Person 클래스의 인스턴스들이 들어있음
#     stairs = []
#
#     for i in range(N):
#         for j in range(N):
#             if board[i][j] == 1:
#                 people.append(Person(i, j))
#             if board[i][j] > 1:
#                 stairs.append((i, j, board[i][j]))
#
#     M = len(people)
#     for p in people:
#         p.set_dis(stairs[0], stairs[1])
#
#
#     for bit_comb in range(1 << M):
#         stair1_Q = []
#         stair2_Q = []
#         for idx in range(M):
#             if bit_comb & (1 << idx) != 0:
#                 stair1_Q.append(people[idx].dis_1)
#             else:
#                 stair2_Q.append(people[idx].dis_2)
#         # stair1_Q와 stair2_Q 를 돌면서 시간 측정
#         stair1_Q.sort()
#         stair2_Q.sort()
#
#         t1 = move(stair1_Q, stairs[0][2])
#         t2 = move(stair2_Q, stairs[1][2])
#
#         if min_time > max(t1, t2):
#             min_time = max(t1, t2)
#
#     print("#{} {}".format(_, min_time))