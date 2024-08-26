# 랜선 자르기

def cut_line(N, start, end):
    if start > end: # 시작값이 끝값보다 커지면 끝값 출력하고 함수 종료
        print(end)
        exit()

    mid = (start + end)//2 # 시작값과 끝값을 더한 후 2로 나눈 몫을 중간값으로 설정
    sum_line = sum(line//mid for line in lines) # 중간값으로 각 선들을 난눈 몫을 모두 더하기

    if sum_line < N: # 더한 값이 목표보다 작으면 중간값의 아래 범위로 재귀
        cut_line(N, start, mid-1)

    else: # 크면 중간값의 윗 범위로 재귀
        cut_line(N, mid+1, end)

K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]
longest = max(lines) # 가장 긴 길이를 기준으로 설정

cut_line(N, 1, longest) # 1을 시작으로 설정(mid 값이 0이 안되게 하려고)