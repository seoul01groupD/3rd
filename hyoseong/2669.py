# 직사각형 네개의 합집합의 면적 구하기

field = [[False] * 101 for _ in range(101)]
extent = 0

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2): # 2563 문제와 비슷하게 해결
            if field[i][j] == False:
                field[i][j] = True
                extent += 1

print(extent)