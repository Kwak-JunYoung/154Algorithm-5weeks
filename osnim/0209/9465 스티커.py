T = int(input())

def sol():
    n = int(input())

    dp = [[0]*(n+1) for i in range(2)]

    array1 = list(map(int, input().split())) # 1행 입력 리스트
    array2 = list(map(int, input().split())) # 2행 입력 리스트

    dp[0][0] = array1[0]
    dp[1][0] = array2[0]

    for j in range(1, n):
        dp[0][j] = max(dp[1][j-1], dp[1][j-2]) + array1[j]
        dp[1][j] = max(dp[0][j-1], dp[0][j-2]) + array2[j]

    print(max(dp[0][n-1], dp[1][n-1]))

for i in range(T):
    sol()