n, m = list(map(int, input().split()))

trees = list(map(int, input().split()))

start = 1

end = max(trees)

while start <= end:
    mid = (start + end) // 2

    acquired = sum([tree - mid for tree in trees if (tree - mid) >= 0])

    if acquired >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)