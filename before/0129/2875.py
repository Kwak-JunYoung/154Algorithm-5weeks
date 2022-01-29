import math
n, m, k = list(map(int, input().split()))

max_team = min(n // 2, m)

left_men = n - max_team * 2
left_women = m - max_team

if left_men + left_women >= k:
    print(max_team)
else:
    required = k - (left_men + left_women)
    print(max_team - math.ceil(required / 3))