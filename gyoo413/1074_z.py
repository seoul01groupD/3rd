n, r, c = map(int, input().split())

def z(n, r, c):
    if n == 0:
        return 0

    temp = 2 ** (n - 1)

    if r < temp and c < temp:
        return z(n - 1, r, c)

    elif r < temp and c >= temp:
        return (temp ** 2) + z(n - 1, r, c - temp)

    elif r >= temp and c < temp:
        return 2 * (temp ** 2) + z(n - 1, r - temp, c)
    
    else:
        return 3 * (temp ** 2) + z(n - 1, r - temp, c - temp)
    
print(z(n, r, c))