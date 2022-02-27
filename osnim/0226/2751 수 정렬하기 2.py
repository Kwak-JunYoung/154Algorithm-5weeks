# 기본 내장 sort 함수 사용
from sys import stdin

n = int(stdin.readline())

#a = [0]*(n+1)
a = []

for _ in range(n):
    a.append(int(stdin.readline()))

a.sort()

#print(a)

for data in a:
    print(data)
    
