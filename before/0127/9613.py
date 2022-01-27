from itertools import combinations
import math

t = int(input())

for _ in range(t):
    num_list = list(map(int, input().split()))[1:]
    combis = list(combinations(num_list, 2))
    print(sum([math.gcd(c[0], c[1]) for c in combis]))