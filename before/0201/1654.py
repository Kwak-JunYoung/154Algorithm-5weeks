k, n = map(int, input().split())

line = [int(input()) for _ in range(k)]

start = 1

end = max(line)

while(start <= end):

    mid = (start + end) // 2

    cnt = sum([i // mid for i in line])

    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)