n = int(input())

ar = []

for _ in range(n):
    x, y = map(int, input().split())
    ar.append((x,y))
    #ar.append([x,y])

ar.sort()

for x, y in ar:
    print(x, y)
    #print(i[0],i[1])