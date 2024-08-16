# 방 배정

N, K = map(int, input().split())
stu_lst = [[0, 0] for _ in range(6)]
room_num = 0

for _ in range(N):
    S, Y = map(int, input().split())
    stu_lst[Y-1][S] += 1 # 학년 마다 성별을 구분해서 튜플로 저장

for i in range(6):
    for j in range(2):
        if stu_lst[i][j] % K: # 값이 K로 나누어지면 몫을, 아니라면 몫+1 이 필요한 방 개수
            room_num += stu_lst[i][j] // K + 1

        else:
            room_num += stu_lst[i][j] // K

print(room_num)