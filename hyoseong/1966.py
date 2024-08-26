# 프린터 큐

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))
    check = [0] * N # 확인할 문서의 위치를 기록할 리스트 준비
    check[M] = 1 # 위치 기록
    count = 0

    while priority:
        length = len(check)

        if priority[0] != max(priority): # 중요도 리스트의 첫 번호가 가장 큰 번호가 아니면
            priority.append(priority.pop(0)) # 리스트 맨 뒤로 이동
            check[0:length-1], check[-1] = check[1:length], check[0] # 위치 기록도 이동

        else: # 맞다면
            priority.pop(0) # 중요도 리스트에서 제거
            count += 1

            if check[0] == 1: # 기록한 위치의 문서가 다음에 인쇄될 차례면 횟수 출력 후 반복문 종료
                print(count)
                break

            else: # 아니라면 맨 앞 위치 제거
                check.pop(0)