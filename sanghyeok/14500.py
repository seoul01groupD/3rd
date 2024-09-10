d_1 = [[0,1],[0,2],[0,3]]   #1자모형
d_2 = [[1,0],[2,0],[3,0]]

d_3 = [[0,1],[1,1],[1,0]]   # 사각형

d_4 = [[1,0],[2,0],[2,1]]   # L자
d_5 = [[1,0],[2,0],[2,-1]]
d_6 = [[0,1],[1,0],[2,0]]
d_7 = [[0,-1],[1,0],[2,0]]
d_8 = [[1,0],[0,1],[0,2]]
d_9 = [[0,-1],[0,-2],[1,0]]
d_10 = [[1,0],[1,-1],[1,-2]]
d_11 = [[1,0],[1,1],[1,2]]

d_12 = [[1,0],[1,1],[2,1]]  # 계단형
d_13 = [[1,0],[1,-1],[2,-1]]
d_14 = [[0,1],[1,0],[1,-1]]
d_15 = [[0,-1],[1,0],[1,1]]

d_16 = [[0,-1],[0,1],[1,0]] # ㅗ 형
d_17 = [[0,-1],[0,1],[-1,0]]
d_18 = [[-1,0],[1,0],[0,1]]
d_19 = [[-1,0],[1,0],[0,-1]]

lst = [d_1,d_2,d_3,d_4,d_5,d_6,d_7,d_8,d_9,d_10,d_11,d_12,d_13,d_14,d_15,d_16,d_17,d_18,d_19]





N, M = map(int, input().split())




arr = [list(map(int, input().split())) for _ in range(N)]

result = []
for row in range(N):
    for col in range(M):
        for i in range(19):
            result2= []
            result2.append(arr[row][col])
            for j in range(3):
                n_row = row + lst[i][j][0]
                n_col = col + lst[i][j][1]
                if 0<=n_row<N and 0<=n_col<M:
                    result2.append(arr[n_row][n_col])
                if len(result2) == 4:
                    a = sum(result2)
                    result.append(a)


print(max(result))

