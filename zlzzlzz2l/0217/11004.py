N, K = map(int, input().split())
nums = list(map(int, input().split()))
nums = sorted(nums)
print(nums[K-1])