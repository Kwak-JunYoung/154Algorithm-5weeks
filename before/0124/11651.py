n = int(input())
coordinates = sorted(sorted([list(map(int, input().split())) for _ in range(n)], key = lambda x: x[0]), key= lambda x: x[1])
for c in coordinates:
    print(c[0], c[1])
