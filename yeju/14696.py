import sys
input = sys.stdin.readline

N = int(input())   # 총 라운드 수
for _ in range(N):
    a = list(map(int,input().split()))
    a_count = a.pop(0)   # A의 총 그림 수
    a.sort(reverse=True)   # 별,동그라미,네모,세모 순으로 정렬
    b = list(map(int,input().split()))
    b_count = b.pop(0)   # B의 총 그림 수
    b.sort(reverse=True)   # 별,동그라미,네모,세모 순으로 정렬

    count = max(a_count,b_count)   # A와 B중 그림이 더 많은 수
    # A와 B의 딱지 수를 맞추기
    if a_count < count:
        for _ in range(count - a_count):
            a.append(0)
    if b_count < count:
        for _ in range(count - b_count):
            b.append(0)

    # 앞에서 부터 하나씩 비교
    for i in range(count):
        if a[i] == b[i]:
            if i == count-1:   # 마지막까지 같으면
                print('D')   # 무승부
            else:
                continue
        elif a[i] < b[i]:   # A < B이면, B
            print('B')
            break
        else:   # A > B이면, A
            print('A')
            break

