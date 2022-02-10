n = int(input())
ar = []

for i in range(n+2):
    ar.append([])
    for j in range(10):
        ar[i].append(0)

for i in range(10):
    ar[1][i] = 1
    ar[2][i] = 10-i

for i in range(3, n+1):
    # 8까지
    for j in range(9):
        sum = 0
        for k in range(9,j-1,-1):
            sum += ar[i-1][k]
        ar[i][j] = sum
    #9로 시작하는 모든 수는 1가지씩
    ar[i][9] = 1

result = 0

for i in range(10):
    result += ar[n][i]

print(result % 10007)



