N , M = map(int, input().split())

arr = [list(map(str, input())) for _ in range(N)]

temp_arr = [[0]*M for _ in range(N)]

cnt = 0
for row in range(N):
    for col in range(M):
