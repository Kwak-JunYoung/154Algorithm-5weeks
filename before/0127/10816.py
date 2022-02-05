import collections

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

counts = collections.Counter(cards)

for t in targets:
    print(counts[t], end=' ')