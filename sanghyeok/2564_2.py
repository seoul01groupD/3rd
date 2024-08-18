# 직사각형 블록의 가로 M, 세로 N
M, N = map(int, input().split())

# 상점의 개수
T = int(input())
stores = []

# 상점의 위치를 저장
for _ in range(T):
    direction, distance = map(int, input().split())
    if direction == 1:  # 북쪽
        stores.append(distance)
    elif direction == 2:  # 남쪽
        stores.append(2 * M + N - distance)
    elif direction == 3:  # 서쪽
        stores.append(2 * (M + N) - distance)
    elif direction == 4:  # 동쪽
        stores.append(M + distance)

# 동근이의 위치
direction, distance = map(int, input().split())
if direction == 1:  # 북쪽
    dg_position = distance
elif direction == 2:  # 남쪽
    dg_position = 2 * M + N - distance
elif direction == 3:  # 서쪽
    dg_position = 2 * (M + N) - distance
elif direction == 4:  # 동쪽
    dg_position = M + distance

# 블록 둘레
perimeter = 2 * (N + M)
min_value = 0

# 각 상점까지의 최단 거리 계산
for store_position in stores:
    # 시계방향 거리
    clockwise_distance = abs(dg_position - store_position)
    # 반시계방향 거리
    counter_clockwise_distance = perimeter - clockwise_distance
    # 최소 거리
    min_value += min(clockwise_distance, counter_clockwise_distance)

print(min_value)
