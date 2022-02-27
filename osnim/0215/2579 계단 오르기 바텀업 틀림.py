n = int(input())

a = [0]*(n)
dp = [0]*(n+1)

for i in range(n):
    a[i] = int(input().rstrip())
    


a.reverse()

#print(a)

#dp[0] = a[0]

for i in range(n):
    dp[i] = max(dp[i-2] + a[i], dp[i-1], dp[i-3] + a[i-1] + a[i])

if dp[i-1] : max()

print(max(dp))