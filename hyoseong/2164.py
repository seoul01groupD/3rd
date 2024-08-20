# 카드2

N = int(input())
queue = [num for num in range(1, N+1)] # 1부터 N까지의 리스트
i = 1

while len(queue) - i > 1: # 값을 제거하는 대신 탐색 범위 좁히기
    queue.append(queue[i]) # i번째 값을 리스트 맨 뒤에 추가
    i += 2 # 첫 값을 제거하고 두번째 값을 밑으로 - 주기 2

print(queue[-1]) # 마지막 값 출력