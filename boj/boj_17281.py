# 야구
# 1: 안타 2: 2루타 3:3루타 4:홈런 0: 아웃
# 1번 선수는 4번 타자

# 가장 많이 득점하는 타순을 찾고, 득점을 구하기

from itertools import permutations

def cal_score(perm):
    out = 0
    score = 0
    idx = 0
    players = [0, 0, 0, 0]  #1루, 2루, 3루
    inning = 0

    while inning < N:
        if idx == 3:
            if batting_infos[inning][0] <= 0:
                out += 1
                if out >= 3:
                    inning += 1
                    out = 0
                    roo = 0
            elif batting_infos[inning][0] <= 3:
                pass

        elif idx < 3:
            if batting_infos[inning][perm[idx]] <= 0:
                out += 1
                if out >= 3:
                    inning += 1
                    out = 0
                    roo = 0
            else:
                roo += batting_infos[inning][perm[idx]]
                if roo > 3:
                    score += roo // 3
                    roo = roo % 3
        elif idx > 3:
            if batting_infos[inning][perm[idx-1]] <= 0:
                out += 1
                if out >= 3:
                    inning += 1
                    out = 0
                    roo = 0
            else:
                roo += batting_infos[inning][perm[idx-1]]
                if roo > 3:
                    score += roo // 3
                    roo = roo % 3

        if idx >= 8:
            idx = 0
        else:
            idx += 1

    return score

# 0~8 를 나열하는 방법에 따라 점수가 달라짐
# 3번타자는 언제나 0번
N =  int(input())
batting_infos = [list(map(int, input().split())) for _ in range(N)]

# 0번은 항상 3번째
# perms 에 있는 tuple 들은 앞에서 0, 1, 2번째 + 4, 5, 6, 7, 8번째가 됨
perms = list(permutations(list(range(1, 9)), 8))
max_score = 0

# for i in range(len(perms)):
#     score = cal_score(perms[i])
#     if score > max_score:
#         max_score = score

cal_score((4, 5, 6, 1, 2, 3, 7, 8))


print(max_score)


