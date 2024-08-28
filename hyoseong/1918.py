# 후위 표기식

exp = input()
stack = []
result = []
priority = {'+':1, '-':1, '*':2, '/':2} # 우선도 표시

for op in exp:
    if op.isalpha(): # 알파벳이면 결과에 추가
        result.append(op)

    elif op == '(': # 여는 괄호면 스택에 추가
        stack.append(op)

    elif op == ')': # 닫는 괄호면 여는 괄호가 나올 때까지 스택의 마지막 요소를 결과에 추가
        while stack[-1] != '(':
            result.append(stack.pop())
        stack.pop() # 마지막으로 여는 괄호 제거

    else: # 연산자라면 우선도를 비교하여 결과, 스택 변경
        while stack and stack[-1] != '(' and priority[stack[-1]] >= priority[op]:
            result.append(stack.pop())
        stack.append(op)

while stack: # 마무리로 결과에 남아있는 스택 추가
    result.append(stack.pop())

print(''.join(result))