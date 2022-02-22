from itertools import combinations
from math import gcd

for i in range(int(input())):
    result = 0
    nums = list(map(int, input().split()))
    for c in combinations(nums[1:], 2):
        result += gcd(c[0], c[1])
    print(result)