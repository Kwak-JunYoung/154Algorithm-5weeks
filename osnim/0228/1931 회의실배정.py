import sys

N = int(sys.stdin.readline().rstrip())
a = []

for i in range(N):
    start, end = map(int, sys.stdin.readline().split())
    diff = end - start
    a.append([start, end, diff])

a.sort(key=lambda x:(x[1], x[0], x[2]))

end = a[0][1]
count = 1

for i in range(1, N):
    if end <= a[i][0]:
        #print(a[i])
        end = a[i][1]
        count += 1

print(count)
