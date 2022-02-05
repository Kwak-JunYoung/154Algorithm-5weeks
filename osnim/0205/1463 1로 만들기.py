N = int(input())

d = [0]*(10**6+1)

for i in range(2, N+1):
    d[i] = d[i-1] + 1

    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1) #1을 더하는 이유 : 아직 연산이 끝난 것이 아니라서

    if i%2==0:
        d[i] = min(d[i], d[i // 2] + 1)

print(d[N])

