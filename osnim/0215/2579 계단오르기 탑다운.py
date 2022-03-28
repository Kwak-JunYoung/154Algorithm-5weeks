#점화식 2개로 풀기

n = int(input())

a = [0]*(n)
dp = [0]*(n)

for i in range(n):
    a[i] = int(input().rstrip())

def sol(n):
    print(sol(n-1))