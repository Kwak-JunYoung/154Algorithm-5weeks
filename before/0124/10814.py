n = int(input())
profiles = sorted([list(map(str, input().split())) for _ in range(n)], key= lambda x: int(x[0]))
for p in profiles:
    print(p[0], p[1])
