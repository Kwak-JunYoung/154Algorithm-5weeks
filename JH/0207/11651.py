n = int(input())
ar=[]

for _ in range(n):
    x, y = map(int, input().split())
    ar.append((x,y))

ar.sort(key=lambda y :(y[1], y[0]))
# ar.sort(key=lambda x : x[1]) #틀림

for x,y in ar:
    print(x,y)
