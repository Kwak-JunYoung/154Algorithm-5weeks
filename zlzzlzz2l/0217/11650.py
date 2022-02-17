nums = [list(map(int, input().split())) for _ in range(int(input()))]
result = sorted(nums)

for i in range(len(nums)):
    print(result[i][0], result[i][1])