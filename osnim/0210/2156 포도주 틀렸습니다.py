n = int(input())

array = [0]*(n+1)

dp1 = [0]*(n+3)
dp2 = [0]*(n+3)
dp3 = [0]*(n+3)

for i in range(1, n+1):
    array[i] = int(input())

# 초기값 필요없음
#dp1[1] = array[1]
#dp2[2] = array[1] + array[2]
#dp3[3] = array[2] + array[3]

for i in range(1, n+1):
    if i%3 == 2:
        dp1[i] = dp1[i-1]
        dp2[i] = dp2[i-1] + array[i]
        dp3[i] = dp3[i - 1] + array[i]

    elif i%3 == 0:
        dp1[i] = dp1[i-1] + array[i]
        dp2[i] = dp2[i - 1]
        dp3[i] = dp3[i - 1] + array[i]

    elif i%3 == 1:
        dp1[i] = dp1[i-1] + array[i]
        dp2[i] = dp2[i - 1] + array[i]
        dp3[i] = dp3[i - 1]

    print(dp1)
    print(dp2)
    print(dp3)


print(max(dp1[n], dp2[n], dp3[n]))