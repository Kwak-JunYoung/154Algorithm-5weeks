n = int(input())

DPtoRight = [0]*(n+1)
DPtoLeft = [0]*(n+1)

a = list(map(int, input().split()))

for i in range(n):
    DPtoRight[i] = 1
    for j in range(i):
        if a[j] < a[i]:
            DPtoRight[i] = max(DPtoRight[j]+1, DPtoRight[i])

for i in range(n-1, -1, -1):
    DPtoLeft[i] = 1
    for j in range(n-1, i, -1):
        if a[j] < a[i]:
            DPtoLeft[i] = max(DPtoLeft[j]+1, DPtoLeft[i])

MAX = 0
for i in range(n):
    if MAX < DPtoRight[i] + DPtoLeft[i]:
        MAX = DPtoRight[i] + DPtoLeft[i]

# +1을 두 번 해서
print(MAX-1)
