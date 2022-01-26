import collections
n = int(input())
print(collections.Counter(sorted([int(input()) for _ in range(n)])).most_common()[0][0])