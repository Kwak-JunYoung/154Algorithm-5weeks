n = int(input())
dp = [0]*(n+1)
a = list(map(int, input().split()))
#dp = a[:] # 시퀀스 객체, 리스트 전체를 가져옴
for i in range(n):
    dp[i] = a[i]
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + a[i])
    print(dp)

print(max(dp))
