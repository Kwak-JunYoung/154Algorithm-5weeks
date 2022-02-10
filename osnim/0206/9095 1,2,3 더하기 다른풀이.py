# 테스트 케이스를 받을 때 마다 출력하게 품
T = int(input())

#테스트 케이스를 저장하는 리스트
array = []

dp = [0] * (12)

dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in range(T):
    #array.append(int(input()))
    n = int(input())
    print(dp[n])

