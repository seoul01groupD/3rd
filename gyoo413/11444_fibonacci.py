n = int(input())

fibo = {}
fibo[n] = 1

def make_fibo(n):
    if n < 1:
        return
    
    k = n // 2
    if n % 2 == 0:
        if not fibo.get(k + 1, False):
            fibo[k + 1] = 1
            make_fibo(k + 1)
        if not fibo.get(k - 1, False):
            fibo[k - 1] = 1
            make_fibo(k - 1)
    else:
        if not fibo.get(k, False):
            fibo[k] = 1
            make_fibo(k)
        if not fibo.get(k + 1, False):
            fibo[k + 1] = 1 
            make_fibo(k + 1)

make_fibo(n)
key = sorted(list(fibo.keys()))

for num in key:
    if num == 0:
        fibo[num] = 0
    elif num == 1:
        fibo[num] = 1
    else:
        if num % 2 == 0:
            fibo[num] = (fibo[num // 2 + 1] ** 2 - fibo[num // 2 - 1] ** 2) % 1000000007
        else:
            fibo[num] = (fibo[num // 2] ** 2 + fibo[num // 2 + 1] ** 2) % 1000000007

print(fibo[n])