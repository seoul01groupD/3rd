N, M, B = map(int, input().split())
heights = {}
min_time = float('inf')

for _ in range(N):
    for height in list(map(int, input().split())):
        if height not in heights: # 높이를 key로, 그 높이의 땅의 개수를 value로 하는 딕셔너리 생성
            heights[height] = 0

        heights[height] += 1

heights = list(sorted(heights.items(), reverse=True)) # (key, value)를 내림차순으로 정렬한 리스트 생성
max_height, min_height = heights[0][0], heights[-1][0]

for num in range(min_height, max_height+1): # 최대, 최소 높이 범위 안의 임의의 높이에 대해
    inven = B
    time = 0

    for height in heights: # 현재 있는 땅의 높이가
        if height[0] > num: # 임의의 높이보다 크면
            amount = (height[0] - num) * height[1] # 떼어낼 땅의 개수
            time += amount * 2 # 2배만큼 시간 증가
            inven += amount # 그만큼 가지고 있는 땅 증가

        else: # 반대의 경우
            amount = (num - height[0]) * height[1] # 붙일 땅의 개수

            if inven >= amount: # 가지고 있는 땅의 개수가 그것보다 많으면
                time += amount
                inven -= amount

            else: # 아니라면 반복문 종료
                break

    else: # 반복문이 정상적으로 끝났다면
        if time <= min_time: # 걸린 시간이 최소 시간이면 변수 갱신
            min_time = time
            current_height = num

print(min_time, current_height)