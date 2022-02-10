nums = range(int(input()))
r = [0 for _ in nums]
for n in nums:
    a, b = map(int, input().split())
    r[n] = a + b

for i in nums:
    print("Case #" + str(i + 1) + ": " + str(r[i]))
