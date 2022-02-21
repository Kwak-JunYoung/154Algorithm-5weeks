nums = input()
nums = sorted(nums, reverse=True)
result = 0

if '0' not in nums:
    print(-1)
else:
    for n in nums:
        result += int(n)
    if result % 3 != 0:
        print(-1)
    else:
        print(''.join(nums))