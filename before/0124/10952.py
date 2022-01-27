ans = []
while True:
    a, b = list(map(int, input().split()))
    if a == 0 and b == 0:
        break
    ans.append(a + b)

for a in ans:
    print(a)
    