n = int(input())

arr = list(map(int, input().split()))

ans = [0] * n

for i in range(n):
    dummy = []
    for j in range(i):
        if arr[i] > arr[j] and ans[i] < ans[j]:
            ans[i] = ans[j]

    ans[i] += 1
        
print(max(ans))