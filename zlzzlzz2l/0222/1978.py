N = int(input())

nums = list(map(int, input().split()))
result = 0
for i in range(N):
    cnt = 0
    if nums[i] == 1:
        continue
    for c in range(1, nums[i]+1):
        if nums[i] % c == 0:
            cnt += 1

    if cnt > 2:
        continue
    else:
        result += 1

print(result)