N = int(input())

K = N//5
result = 0
while True:
    if K == 0:
        if N%3 == 0:
            result = N//3
            break
        else:
            result = -1
            break
    elif (N-K*5)%3 !=0:
        K-=1
    else:
        result = K+(N-K*5)//3
        break

print(result)