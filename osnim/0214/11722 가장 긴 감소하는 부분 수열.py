n = int(input())

a = list(map(int, input().split()))

dp = [0] * (n+1)

for i in range(n):
    dp[i] = 1
    for j in range(i):
        if a[j] > a[i]:
            dp[i] = max(dp[j]+1, dp[i])
    print(dp)

#print(dp[n-1]) 이라서 틀림)
print(max(dp))

"""
for i in range(n, 0, -1):
    print(dp[i])
"""
"""
for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[j]+1, dp[i])

    print(dp)
"""

