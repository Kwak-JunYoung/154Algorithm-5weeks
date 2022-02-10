"""
n = int(input())

#테스트 케이스를 저장하는 리스트
array = []

for i in range(n):
    array.append(int(input()))

dp = [0] * (12)

dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4

j = 0

for i in range(4, 11+1):
    if j >= n:
        break

    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    if array[j] == i:
        print(dp[i])
        j += 1
"""

# 위에는 한번에 출력해서 그런가 틀렸습니다. 뜸
