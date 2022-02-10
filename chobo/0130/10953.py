nums = range(int(input()))
r = [0 for i in nums]
for n in nums:
    a, b = map(int, input().split(","))
    r[n] = a + b

for n in nums:
    print(r[n])