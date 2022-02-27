n = int(input())

a = [0] * (n+1)
# = [0] * (n+1)

for _ in range(n):
    i = int(input())
    a[i] += 1  # 계수 정렬, 값과 인덱스가 같은 경우 count 1

#print(a)

for i in range(1 ,n+1):
    for j in range(a[i]):
        print(i)
