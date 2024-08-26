# 스택 수열

import sys

N = int(sys.stdin.readline())
count = [0] * N
stack = []

for i in range(N):
    order = int(sys.stdin.readline())
    count[order-1] = i # 값을 인덱스로 순서 리스트 설정

num = 1
order = 0
poped = 0
symbols = []

while poped != N: # 맞은 숫자의 개수가 N이 될 때까지 반복 

    if stack == [] or count[stack[-1] - 1] != order: # 스택이 비어있거나 스택 마지막 요소의 순서가 아니면
        stack.append(num) # 숫자와 '+' 기호를 각각 추가
        symbols.append('+')

        if num > N: # 숫자가 N보다 크면 불가능한 것이므로 종료
            print('NO')
            exit(0)

        num += 1

    elif count[stack[-1] - 1] == order: # 순서가 왔다면
        stack.pop() # 스택에 넣었던 숫자 제거
        symbols.append('-') # '-' 기호 추가
        order += 1 # 순서, 맞은 숫자 개수 1씩 증가
        poped += 1

for symbol in symbols:
    print(symbol)