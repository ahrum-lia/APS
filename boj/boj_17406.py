# 배열돌리기4
from itertools import permutations



def circulate(array, cond_seq, conds):
    global min_val
    def move(stt, end):
        start_val = array[stt[0]][stt[1]]
        nxt = (stt[0]+1, stt[1])
        while nxt[0] <= end[0]:
            array[nxt[0]-1][nxt[1]] = array[nxt[0]][nxt[1]]
            nxt = (nxt[0]+1, nxt[1])
        nxt = (end[0], stt[1]+1)

        while nxt[1] <= end[1]:
            array[nxt[0]][nxt[1]-1] = array[nxt[0]][nxt[1]]
            nxt = (nxt[0], nxt[1] + 1)
        nxt = (end[0]-1, end[1])

        while nxt[0] >= stt[0]:
            array[nxt[0]+1][nxt[1]] = array[nxt[0]][nxt[1]]
            nxt = (nxt[0]-1, nxt[1])
        nxt = (stt[0], end[1]-1)

        while nxt[1] >= stt[1]:
            array[nxt[0]][nxt[1]+1] = array[nxt[0]][nxt[1]]
            nxt = (nxt[0], nxt[1]-1)
        array[stt[0]][stt[1]+1] = start_val


    res = 0xffffff

    for cond_idx in cond_seq:
        cond = conds[cond_idx]
        stt = (cond[0]-cond[2]-1, cond[1]-cond[2]-1) # 왼쪽 끝 좌표
        end = (cond[0]+cond[2]-1, cond[1]+cond[2]-1) # 오른쪽 끝 좌표

        while stt != end:
            move(stt, end)
            stt = (stt[0]+1, stt[1]+1)
            end = (end[0]-1, end[1]-1)


    # 돌리고 난 후 arr 행값의 최솟값을 찾아서 min_val 과 비교해서 갱신
    for i in range(N):
        tmp = sum(array[i])
        if tmp < res:
            res = tmp

    if min_val > res:
        min_val = res

    return


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
copied_arr = [arr[i][:] for i in range(N)]
conds = [tuple(map(int, input().split())) for __ in range(K)]
min_val = 0xffffff


cond_perm = permutations(tuple(range(K)), K)

# conds의 갯수만큼 순열을 만들어서 배열을 돌려보고 arr의 값을 구해서 최솟값을 갱신한다
for cond_seq in cond_perm:
    circulate(arr, cond_seq, conds)
    arr = [copied_arr[j][:] for j in range(N)]

print(min_val)




