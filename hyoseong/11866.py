# 요세푸스 문제 0

N, K = map(int, input().split())
queue = [num for num in range(1, N+1)] # 1부터 N까지의 리스트
i = 0

while i < N:
    for _ in range(K-1): # K번째 사람을 제거하는 대신
        queue.append(queue.pop(i)) # 그 사람까지의 사람들을 리스트 맨 뒤에 추가
    i += 1 # 그 사람은 그대로 두고 그 뒤부터 다시 반복

print('<' + ', '.join(map(str, queue)) + '>')