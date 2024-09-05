from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
tanghuru = deque(map(int, input().split()))
dict_tang = {}
for i in range(n):
    if dict_tang.get(tanghuru[i], False):
        dict_tang[tanghuru[i]] += 1
    else:
        dict_tang[tanghuru[i]] = 1

while True:
    k = len(tanghuru)
    length = len(set(tanghuru))
    if length < 3:
        break
    
    