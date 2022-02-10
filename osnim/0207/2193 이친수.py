n = int(input())

dp0 = [0]*(n+3) # 끝 자리가 0인 이친수를 저장하기 위한 리스트
dp1 = [0]*(n+3) # 끝 자리가 1인 이친수를 저장하기 위한 리스트

dp0[1] = 0
dp1[1] = 1

dp0[2] = 1
dp1[2] = 0

dp0[3] = 1
dp1[3] = 1

for i in range(4, n+2):
    dp0[i] = dp0[i-1] +dp0[i-2]
    dp1[i] = dp1[i-1] +dp1[i-2]

print(dp0[n]+dp1[n])