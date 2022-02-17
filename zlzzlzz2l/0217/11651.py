nums = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    nums.append([y, x])

nums = sorted(nums)
for i in range(len(nums)):
    print(nums[i][1], nums[i][0])