# 체스판 다시 칠하기

N, M = map(int, input().split())
board = []
min_change = 32 # 바꿀 정사각형의 최대 개수 

for _ in range(N):
    board.append(input())

for i in range(N - 7):
    for j in range(M - 7): # 8×8 범위를 만들기 위해 거리가 7 이상 떨어진 곳의 정사각형 선정
        start_b = 0
        start_w = 0

        for p in range(i, i+8):
            for q in range(j, j+8):
                if (p+q) % 2 == 0: # 좌표의 x, y 값이 모두 짝수거나 홀수면
                    if board[p][q] == 'B':
                        start_w += 1
                    else:
                        start_b += 1

                else: # 반대로 하나는 짝수고 하나는 홀수면
                    if board[p][q] == 'B':
                        start_b += 1
                    else:
                        start_w += 1

        if start_b < start_w and start_b < min_change: # 체스판의 맨 왼쪽 칸을 검은색으로 했을 때
            min_change = start_b

        elif start_w < start_b and start_w < min_change: # 반대로 흰색으로 했을 때
            min_change = start_w

print(min_change) # 두 가지 경우에서 가장 적게 바꾸는 경우를 선택하여 출력